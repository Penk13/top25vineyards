# Generated by Django 3.2 on 2021-09-28 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0005_contentpage_meta_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentpage',
            name='ad_manager',
            field=models.TextField(blank=True),
        ),
    ]