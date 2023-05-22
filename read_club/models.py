import datetime

from datetime import date
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


def max_value_current_year(value: str):
    """ Проверка текущего года и введенного в поле. """
    return MaxValueValidator(Book.current_year())(value)


class Book(models.Model):
    """ Модель книга. """
    verbose_name = "Задача"
    ordering = ["-updated", "-created"]

    @staticmethod
    def current_year():
        """ Получаем текущий год. """
        return datetime.date.today().year

    title = models.CharField(max_length=120, null=False, unique=True, blank=True)
    description = models.TextField(max_length=260, null=False, blank=True)
    preview = models.ImageField(upload_to='static/previews', null=False)
    author = models.CharField(max_length=120, null=False, blank=True)
    published = models.IntegerField(
        default=current_year(),
        validators=[MinValueValidator(1990), max_value_current_year],
        blank=True
    )
    publisher = models.CharField(max_length=120, null=False, blank=True)

    def __str__(self) -> str:
        """Строчное представление объекта."""
        return f"{self.title} {self.author} издательство {self.publisher} {self.published} г."

    def events(self):
        """ Все события с отмеченной книгой. """
        return Event.objects.filter(book=self.id)

    def reviews(self):
        """ Все подтвержденные рецензии на книги. """
        return Review.objects.filter(book=self.id, is_approve=True)


class Event(models.Model):
    """ Модель события. """
    verbose_name = "Событие"

    ordering = ["-updated", "-created"]

    title = models.CharField(max_length=120, null=False, blank=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT, null=False, blank=True)
    start = models.DateField(default=date.today, null=False, blank=True)
    finish = models.DateField(null=False, blank=True)

    def __str__(self) -> str:
        """Строчное представление объекта."""
        book_title = '---'

        if self.book:
            book_title = self.book.title

        return f"{self.title} (с {self.start} по {self.finish}), книга {book_title}"

    @property
    def is_finished(self):
        return date.today() >= self.finish

    @property
    def is_subscribe(self):
        return bool(Subscribe.objects.filter(event=self.pk).first())


class Note(models.Model):
    """ Модель заметки. """
    verbose_name = "Заметки"

    ordering = ["-updated", "-created"]

    personal_count = 10

    title = models.CharField(max_length=120, null=False, blank=True)
    description = models.TextField(null=False, blank=True)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Строчное представление объекта."""
        book_title = '---'

        if self.book:
            book_title = self.book.title

        return f"{book_title} - {self.title}: {self.description[1:22]}..."


class Review(models.Model):
    """ Модель рецензии. """
    verbose_name = "Рецензия"

    ordering = ["-updated", "-created"]

    title = models.CharField(max_length=120, null=False)
    description = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    is_approve = models.BooleanField(default=False, null=False)

    def __str__(self) -> str:
        """Строчное представление объекта."""
        book_title = '---'

        if self.book:
            book_title = self.book.title

        return f"{book_title} - {self.title}: {self.description[1:30]}..."


class Subscribe(models.Model):
    """ Модель подписок. """
    verbose_name = "Подписки"
    ordering = ["-created"]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        """Строчное представление объекта."""
        event_start = '----'
        event_finish = '----'
        book_title = '---'

        if self.event:
            event_start = self.event.start
            event_finish = self.event.finish

            if self.event.book:
                book_title = self.event.book.title

        return f"{book_title} {event_start} - {event_finish}"

    def is_book_has_review(self):
        """ Проверяем, что книга уже имеет отзыв. """
        return bool(Review.objects.filter(book=self.event.book, user=self.user).first())

    def is_event_has_enough_notes(self):
        """ Проверяем, что пользователь не оставит больше заметок, чем указано в моделе. """
        return self.get_event_notes().count() >= Note.personal_count

    def get_event_notes(self):
        """ Получить все заметки пользователя по событию. """
        return Note.objects.filter(event=self.event, user=self.user)
