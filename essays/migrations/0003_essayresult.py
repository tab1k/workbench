# Generated by Django 4.2.2 on 2023-07-19 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("courses", "0010_alter_course_course_type"),
        ("essays", "0002_alter_essay_options_essay_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="EssayResult",
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
                ("essay_text", models.TextField()),
                ("is_passed", models.BooleanField(default=False)),
                (
                    "lesson",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="courses.lesson"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Результат эссе",
                "verbose_name_plural": "Результаты эссе",
            },
        ),
    ]