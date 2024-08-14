# Generated by Django 5.0.7 on 2024-08-02 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0004_alter_part_pdf_file_alter_part_piece"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="part",
            options={"ordering": ["instrument", "part_number"]},
        ),
        migrations.AlterUniqueTogether(
            name="part",
            unique_together={("instrument", "part_number")},
        ),
    ]
