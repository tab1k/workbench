# Generated by Django 4.2.4 on 2024-01-15 21:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0020_course_start_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="start_date",
            field=models.DateField(auto_created=True, blank=True, null=True),
        ),
    ]