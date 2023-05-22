from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from read_club.models import Book, Event, Note, Review, Subscribe
from django_seed import Seed


class Command(BaseCommand):
    """ Команда сидирования. """
    def handle(self, *args, **options):
        """ Выполнение команды. """
        seeder = Seed.seeder('ru_RU')
        seeder.add_entity(Book, 6, {
            'author': lambda x: seeder.faker.name(),
            'publisher': lambda x: seeder.faker.text(15),
            'published': lambda x: seeder.faker.year()
        })
        seeder.add_entity(Event, 4)
        seeder.add_entity(User, 3)
        seeder.add_entity(Subscribe, 6)
        seeder.add_entity(Note, 20)
        seeder.add_entity(Review, 10)

        seeder.execute()

        self.stdout.write(self.style.SUCCESS('Successfully seed'))

