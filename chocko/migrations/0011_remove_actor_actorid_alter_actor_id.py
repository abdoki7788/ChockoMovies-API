# Generated by Django 4.1.4 on 2022-12-22 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chocko", "0010_alter_movie_actors_alter_movie_companies_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="actor",
            name="actorid",
        ),
        migrations.AlterField(
            model_name="actor",
            name="id",
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]