# Generated by Django 3.2 on 2022-02-11 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vineyards', '0039_auto_20220209_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='sidebar',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='vineyard',
            name='sidebar',
            field=models.TextField(blank=True),
        ),
    ]
