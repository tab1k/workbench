# Generated by Django 4.2.2 on 2023-08-28 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0016_notification_students"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="notification",
            options={
                "verbose_name": "Объявление курсу",
                "verbose_name_plural": "Объявление курсам",
            },
        ),
        migrations.AddField(
            model_name="lesson",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="courses.course",
            ),
        ),
    ]