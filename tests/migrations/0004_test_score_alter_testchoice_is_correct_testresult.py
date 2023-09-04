# Generated by Django 4.2.2 on 2023-07-13 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0009_alter_lesson_video"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tests", "0003_alter_test_options_alter_testchoice_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="test",
            name="score",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="testchoice",
            name="is_correct",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="TestResult",
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
                ("score", models.PositiveIntegerField()),
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
                "verbose_name": "Результат теста",
                "verbose_name_plural": "Результаты тестов",
            },
        ),
    ]