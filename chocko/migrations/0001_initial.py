# Generated by Django 4.1.4 on 2022-12-21 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Actor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("actorid", models.CharField(max_length=20, unique=True)),
                ("name", models.CharField(max_length=50)),
                ("image", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("slug", models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("slug", models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "movieid",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=50)),
                ("full_title", models.CharField(max_length=100)),
                ("release_date", models.DateField()),
                ("type", models.CharField(max_length=20)),
                ("plot", models.TextField()),
                ("country", models.CharField(max_length=20)),
                ("imdb_rating", models.DecimalField(decimal_places=1, max_digits=1)),
                ("image", models.URLField(blank=True)),
                ("trailer", models.URLField(blank=True)),
                ("actors", models.ManyToManyField(to="chocko.actor")),
                ("companies", models.ManyToManyField(to="chocko.company")),
                ("genres", models.ManyToManyField(to="chocko.category")),
            ],
        ),
    ]
