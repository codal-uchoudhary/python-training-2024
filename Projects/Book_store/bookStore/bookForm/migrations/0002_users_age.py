# Generated by Django 4.2.10 on 2024-02-19 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookForm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='age',
            field=models.IntegerField(null='True'),
            preserve_default='True',
        ),
    ]
