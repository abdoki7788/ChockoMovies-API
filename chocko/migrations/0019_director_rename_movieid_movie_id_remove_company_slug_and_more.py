# Generated by Django 4.1.4 on 2023-01-05 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chocko", "0018_movie_saves"),
    ]

    operations = [
        migrations.CreateModel(
            name="Director",
            fields=[
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=50)),
                ("image", models.URLField()),
            ],
        ),
        migrations.RenameField(
            model_name="movie",
            old_name="movieid",
            new_name="id",
        ),
        migrations.RemoveField(
            model_name="company",
            name="slug",
        ),
        migrations.AddField(
            model_name="movie",
            name="stars",
            field=models.ManyToManyField(blank=True, to="chocko.actor"),
        ),
        migrations.AddField(
            model_name="movie",
            name="timeString",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="movie",
            name="votes_count",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="id",
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name="movie",
            name="director",
            field=models.ManyToManyField(
                blank=True, related_name="works", to="chocko.director"
            ),
        ),
    ]
