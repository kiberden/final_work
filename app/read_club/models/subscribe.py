from django.contrib.auth.models import User
from django.db import models

from app.read_club.models.event import Event


class Subscribe(models.Model):
    """ Модель подписок. """
    verbose_name = "Подписки"
    ordering = ["-created"]

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, null=False)
    event = models.OneToOneField(Event, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        """Строчное представление объекта."""
        return f"{self.event.book.title} {self.event.start} - {self.event.finish}"
