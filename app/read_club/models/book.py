import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Book(models.Model):
    """ Модель книга. """
    verbose_name = "Задача"
    ordering = ["-updated", "-created"]

    @staticmethod
    def current_year():
        """ Получаем текущий год. """
        return datetime.date.today().year

    @staticmethod
    def max_value_current_year(value):
        """ Проверка текущего года и введенного в поле. """
        return MaxValueValidator(Book.current_year())(value)

    title = models.CharField(max_length=120, null=False)
    description = models.CharField(max_length=260, null=False)
    preview = models.FileField(upload_to='preview', max_length=25)
    author = models.CharField(max_length=120, null=False)
    published = models.IntegerField(
        default=current_year(),
        validators=[MinValueValidator(1990), max_value_current_year]
    )
    publisher = models.CharField(max_length=120, null=False)

    def __str__(self) -> str:
        """Строчное представление объекта."""
        return f"{self.author} {self.title} {self.publisher} ({self.published} г. издания)"
