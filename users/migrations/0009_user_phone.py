# Generated by Django 4.2.4 on 2024-01-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0008_user_address_user_city_user_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="phone",
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
