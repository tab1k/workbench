# Generated by Django 4.2.2 on 2023-07-19 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0009_alter_lesson_video"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="course_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="courses",
                to="courses.coursetype",
            ),
        ),
    ]
