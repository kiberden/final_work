from django.contrib.auth.models import User
from django.db import models

from read_club.models.book import Book


class Review(models.Model):
    """ Модель рецензии. """
    verbose_name = "Рецензия"

    ordering = ["-updated", "-created"]

    title = models.CharField(max_length=120, null=False)
    description = models.TextField(null=False)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, null=False)
    book = models.OneToOneField(Book, on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        """Строчное представление объекта."""
        return f"{self.book.title} - {self.title}: {self.description[1:30]}..."
