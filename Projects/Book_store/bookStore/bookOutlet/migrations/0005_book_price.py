# Generated by Django 5.0.1 on 2024-02-05 04:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bookOutlet", "0004_remove_book_value"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="price",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
