# Generated by Django 3.2 on 2021-12-07 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vineyards', '0030_reviewandrating_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='meta_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='vineyard',
            name='meta_description',
            field=models.TextField(blank=True),
        ),
    ]