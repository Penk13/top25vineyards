# Generated by Django 3.2 on 2021-12-07 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0021_alter_contentpage_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentpage',
            name='meta_description',
            field=models.TextField(blank=True),
        ),
    ]
