# Generated by Django 3.2 on 2021-09-28 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vineyards', '0006_auto_20210927_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='meta_keywords',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='vineyard',
            name='meta_keywords',
            field=models.TextField(blank=True),
        ),
    ]
