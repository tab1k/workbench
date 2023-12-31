# Generated by Django 4.2.2 on 2023-07-05 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0004_coursetype_course_course_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="category",
        ),
        migrations.AlterField(
            model_name="course",
            name="course_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="courses.coursetype"
            ),
        ),
    ]
