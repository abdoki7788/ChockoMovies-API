# Generated by Django 4.1.4 on 2023-01-17 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("chocko", "0023_remove_movie_stars"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="director",
            name="image",
        ),
    ]
