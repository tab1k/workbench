# Generated by Django 4.2.4 on 2024-03-23 03:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0026_lesson_stream_url_alter_lesson_video"),
    ]

    operations = [
        migrations.CreateModel(
            name="TemporaryToken",
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
                ("token", models.CharField(max_length=255)),
                ("expiration_time", models.DateTimeField()),
            ],
        ),
    ]
