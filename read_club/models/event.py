from datetime import date

from django.db import models

from read_club.models.book import Book


class Event(models.Model):
    """ Модель события. """
    verbose_name = "Событие"

    ordering = ["-updated", "-created"]

    title = models.CharField(max_length=120, null=False)
    book = models.OneToOneField(Book, on_delete=models.PROTECT, null=False)
    start = models.DateField(default=date.today, null=False)
    finish = models.DateField(null=False)

    def __str__(self) -> str:
        """Строчное представление объекта."""
        return f"{self.title} (с {self.start} по {self.finish}), книга {self.book.title}"
