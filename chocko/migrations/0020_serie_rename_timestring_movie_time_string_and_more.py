# Generated by Django 4.1.4 on 2023-01-17 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "chocko",
            "0019_director_rename_movieid_movie_id_remove_company_slug_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Serie",
            fields=[
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=50)),
                ("full_title", models.CharField(max_length=100)),
                ("release_date", models.DateField()),
                ("plot", models.TextField()),
                ("imdb_rating", models.DecimalField(decimal_places=1, max_digits=2)),
                ("votes_count", models.IntegerField(blank=True, null=True)),
                ("image", models.URLField(blank=True)),
                ("trailer", models.URLField(blank=True)),
                ("time", models.IntegerField()),
                ("time_string", models.CharField(blank=True, max_length=20, null=True)),
                ("year_end", models.IntegerField(null=True)),
                (
                    "actors",
                    models.ManyToManyField(
                        blank=True, related_name="series", to="chocko.actor"
                    ),
                ),
                (
                    "companies",
                    models.ManyToManyField(
                        blank=True, related_name="series", to="chocko.company"
                    ),
                ),
                (
                    "content_rating",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="series",
                        to="chocko.contentrating",
                    ),
                ),
                (
                    "countries",
                    models.ManyToManyField(
                        blank=True, related_name="series", to="chocko.country"
                    ),
                ),
                (
                    "director",
                    models.ManyToManyField(
                        blank=True, related_name="series", to="chocko.director"
                    ),
                ),
                (
                    "genres",
                    models.ManyToManyField(
                        blank=True, related_name="serie_items", to="chocko.genre"
                    ),
                ),
                (
                    "saves",
                    models.ManyToManyField(
                        blank=True,
                        related_name="saved_series",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("stars", models.ManyToManyField(blank=True, to="chocko.actor")),
            ],
        ),
        migrations.RenameField(
            model_name="movie",
            old_name="timeString",
            new_name="time_string",
        ),
        migrations.RemoveField(
            model_name="movie",
            name="type",
        ),
        migrations.AlterField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(
                blank=True, related_name="movies", to="chocko.actor"
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="companies",
            field=models.ManyToManyField(
                blank=True, related_name="movies", to="chocko.company"
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="countries",
            field=models.ManyToManyField(
                blank=True, related_name="movies", to="chocko.country"
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="director",
            field=models.ManyToManyField(
                blank=True, related_name="movies", to="chocko.director"
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(
                blank=True, related_name="movie_items", to="chocko.genre"
            ),
        ),
        migrations.DeleteModel(
            name="MovieType",
        ),
    ]
