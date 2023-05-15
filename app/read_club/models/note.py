from django.contrib.auth.models import User
from django.db import models

from read_club.models.book import Book
from read_club.models.event import Event


class Note(models.Model):
    """ Модель заметки. """
    verbose_name = "Заметки"

    ordering = ["-updated", "-created"]

    title = models.CharField(max_length=120, null=False)
    description = models.TextField(null=False)
    book = models.OneToOneField(Book, on_delete=models.DO_NOTHING, primary_key=True)
    event = models.OneToOneField(Event, on_delete=models.DO_NOTHING)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self) -> str:
        """Строчное представление объекта."""
        return f"{self.book.title} - {self.title}: {self.description[1:22]}..."
