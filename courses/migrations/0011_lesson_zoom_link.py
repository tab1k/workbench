# Generated by Django 4.2.2 on 2023-07-20 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0010_alter_course_course_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="zoom_link",
            field=models.URLField(blank=True, null=True),
        ),
    ]
