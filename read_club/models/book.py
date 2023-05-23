import datetime

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
