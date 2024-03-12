# Generated by Django 4.2.10 on 2024-03-11 11:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0007_comments"),
        ("account", "0002_usercontent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usercontent",
            name="bookmarks",
            field=models.ManyToManyField(related_name="bookmark_list", to="blog.post"),
        ),
    ]
