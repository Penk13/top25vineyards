# Generated by Django 3.2 on 2021-09-25 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentpage',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
