# Generated by Django 5.0.7 on 2024-08-14 12:48

import django.core.validators
import django.db.models.deletion
import gdstorage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Piece",
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
                ("composer", models.CharField(blank=True, max_length=100)),
                ("arranged_by", models.CharField(blank=True, max_length=100)),
                ("genre", models.CharField(max_length=100)),
                ("mc_location", models.CharField(blank=True, max_length=100)),
                (
                    "band_arrangement",
                    models.CharField(
                        choices=[
                            ("Full-band", "Full-band"),
                            ("Flexi-band", "Flexi-band"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Part",
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
                ("instrument", models.CharField(max_length=100)),
                (
                    "part_number",
                    models.SmallIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(5),
                        ],
                    ),
                ),
                (
                    "pdf_file",
                    models.FileField(
                        storage=gdstorage.storage.GoogleDriveStorage(), upload_to="pdf/"
                    ),
                ),
                (
                    "piece",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="parts",
                        to="library.piece",
                    ),
                ),
            ],
            options={
                "ordering": ["instrument", "part_number"],
                "unique_together": {("instrument", "part_number")},
            },
        ),
    ]