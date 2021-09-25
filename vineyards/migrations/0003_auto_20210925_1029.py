# Generated by Django 3.2 on 2021-09-25 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vineyards', '0002_auto_20210921_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='vineyard',
            name='owner_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='vineyard',
            name='wine_rg',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vineyard',
            name='wine_rg_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='vineyard',
            name='wines',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vineyard',
            name='wines_url',
            field=models.URLField(blank=True),
        ),
    ]
