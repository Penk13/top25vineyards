# Generated by Django 3.2 on 2021-10-03 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vineyards', '0020_auto_20211001_2217'),
        ('pages_app', '0014_navbar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navbar',
            name='types',
        ),
        migrations.AddField(
            model_name='navbar',
            name='page',
            field=models.ManyToManyField(blank=True, to='pages_app.ContentPage'),
        ),
        migrations.AddField(
            model_name='navbar',
            name='region',
            field=models.ManyToManyField(blank=True, to='vineyards.Region'),
        ),
    ]
