# Generated by Django 4.2.10 on 2024-02-15 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0003_alter_post_image_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="author",
            name="email",
        ),
        migrations.RemoveField(
            model_name="author",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="author",
            name="last_name",
        ),
        migrations.AddField(
            model_name="author",
            name="bio",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="author",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
