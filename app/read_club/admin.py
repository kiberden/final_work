from django.contrib import admin

from app.read_club.models.book import Book
from app.read_club.models.event import Event
from app.read_club.models.subscribe import Subscribe

admin.site.register(Book)
admin.site.register(Event)
admin.site.register(Subscribe)
