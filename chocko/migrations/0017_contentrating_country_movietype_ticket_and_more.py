# Generated by Django 4.1.4 on 2023-01-05 05:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chocko", "0016_comment_send_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContentRating",
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
                ("rating", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Country",
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
                ("display_name", models.CharField(blank=True, max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name="MovieType",
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
            ],
        ),
        migrations.CreateModel(
            name="Ticket",
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
                ("email", models.EmailField(max_length=254)),
                ("content", models.TextField()),
                ("send_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="actor",
            name="birth_date",
        ),
        migrations.RemoveField(
            model_name="actor",
            name="summary",
        ),
        migrations.RemoveField(
            model_name="movie",
            name="country",
        ),
        migrations.AlterField(
            model_name="comment",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="target",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="chocko.movie",
            ),
        ),
        migrations.CreateModel(
            name="Group",
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
                ("title", models.CharField(max_length=50)),
                (
                    "items",
                    models.ManyToManyField(
                        related_name="added_groups", to="chocko.movie"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="movie",
            name="countries",
            field=models.ManyToManyField(
                blank=True, related_name="items", to="chocko.country"
            ),
        ),
        migrations.AddField(
            model_name="movie",
            name="type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="items",
                to="chocko.movietype",
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="content_rating",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="movies",
                to="chocko.contentrating",
            ),
        ),
    ]
