# Generated by Django 5.1.3 on 2025-02-24 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="pincode",
            field=models.IntegerField(default=628501),
        ),
    ]
