# Generated by Django 4.2.10 on 2024-02-12 13:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_rename_data_post_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image_name",
            field=models.ImageField(upload_to="static/blog/"),
        ),
    ]
