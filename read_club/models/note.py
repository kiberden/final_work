from django.contrib.auth.models import User
from django.db import models

from read_club.models.book import Book
from read_club.models.event import Event


class Note(models.Model):
    """ Модель заметки. """
    verbose_name = "Заметки"

    ordering = ["-updated", "-created"]

    title = models.CharField(max_length=120, null=False, blank=True)
    description = models.TextField(null=False, blank=True)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    event = models.OneToOneField(Event, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Строчное представление объекта."""
        book_title = '---'

        if self.book:
            book_title = self.book.title

        return f"{book_title} - {self.title}: {self.description[1:22]}..."
