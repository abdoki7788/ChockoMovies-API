# Generated by Django 4.1.4 on 2023-03-07 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chocko", "0030_group_slug_alter_group_items"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="group",
            name="title",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
