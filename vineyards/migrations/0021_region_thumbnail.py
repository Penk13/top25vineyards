# Generated by Django 3.2 on 2021-10-07 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vineyards', '0020_auto_20211001_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='thumbnail',
            field=models.ImageField(blank=True, max_length=255, upload_to='thumbnail-region'),
        ),
    ]
