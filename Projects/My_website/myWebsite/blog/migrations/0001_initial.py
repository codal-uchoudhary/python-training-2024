# Generated by Django 5.0.1 on 2024-02-06 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('excerpt', models.CharField(max_length=200)),
                ('image_name', models.CharField(max_length=30)),
                ('data', models.DateField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='blog.author')),
                ('tags', models.ManyToManyField(to='blog.tag')),
            ],
        ),
    ]
