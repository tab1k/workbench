# Generated by Django 4.2.2 on 2023-06-26 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_user_role_alter_user_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name": "user", "verbose_name_plural": "users"},
        ),
        migrations.RemoveField(
            model_name="user",
            name="image",
        ),
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("student", "Студент"),
                    ("curator", "Куратор"),
                    ("admin", "Администратор"),
                ],
                default="student",
                max_length=10,
            ),
        ),
    ]