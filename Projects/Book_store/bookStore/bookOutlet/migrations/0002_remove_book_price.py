# Generated by Django 5.0.1 on 2024-02-04 13:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bookOutlet", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="price",
        ),
    ]
