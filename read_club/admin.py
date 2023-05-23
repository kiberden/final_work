from django.contrib import admin

from read_club.models import Book, Review, Event, Note, Subscribe

admin.site.register(Book)
admin.site.register(Event)
admin.site.register(Note)
admin.site.register(Review)
admin.site.register(Subscribe)
