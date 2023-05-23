from django.contrib.auth.models import User
from django.db import models

from read_club.models.event import Event


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
