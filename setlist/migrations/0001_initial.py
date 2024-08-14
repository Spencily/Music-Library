# Generated by Django 5.0.7 on 2024-07-31 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Setlist",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True)),
                ("pieces", models.ManyToManyField(to="library.piece")),
            ],
        ),
    ]
