# Generated by Django 3.2 on 2022-07-03 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vineyards', '0062_vineyard_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vineyard',
            old_name='tags',
            new_name='filter_tags',
        ),
    ]
