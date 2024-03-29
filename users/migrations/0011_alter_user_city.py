# Generated by Django 4.2.4 on 2024-01-16 23:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0010_alter_user_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="city",
            field=models.CharField(
                choices=[
                    ("tse", "Астана"),
                    ("ala", "Алматы"),
                    ("msq", "Москва"),
                    ("kiev", "Киев"),
                    ("bishkek", "Бишкек"),
                    ("tashkent", "Ташкент"),
                ],
                default="tse",
                max_length=20,
            ),
        ),
    ]
