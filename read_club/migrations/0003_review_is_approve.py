# Generated by Django 4.2.1 on 2023-05-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read_club', '0002_alter_event_book_alter_note_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='is_approve',
            field=models.BooleanField(default=False),
        ),
    ]