from datetime import date

from django.db import models

from read_club.models.book import Book


class Event(models.Model):
    """ Модель события. """
    verbose_name = "Событие"

    ordering = ["-updated", "-created"]

    title = models.CharField(max_length=120, null=False, blank=True)
    book = models.OneToOneField(Book, on_delete=models.PROTECT, null=False, blank=True)
    start = models.DateField(default=date.today, null=False, blank=True)
    finish = models.DateField(null=False, blank=True)

    def __str__(self) -> str:
        """Строчное представление объекта."""
        book_title = '---'

        if self.book:
            book_title = self.book.title

        return f"{self.title} (с {self.start} по {self.finish}), книга {book_title}"
