# Generated by Django 3.2 on 2022-01-04 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0021_billboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='billboard',
            name='url',
            field=models.URLField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
