# Generated by Django 3.2 on 2021-10-12 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_autoblogging_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoblogging',
            name='items',
            field=models.IntegerField(default=15),
        ),
    ]
