# Generated by Django 4.2.4 on 2024-03-23 08:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0027_temporarytoken"),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="home_work",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
    ]
