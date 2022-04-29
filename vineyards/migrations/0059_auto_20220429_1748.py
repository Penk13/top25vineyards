# Generated by Django 3.2 on 2022-04-29 10:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vineyards', '0058_auto_20220429_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='add_date',
        ),
        migrations.RemoveField(
            model_name='region',
            name='isvalidated',
        ),
        migrations.RemoveField(
            model_name='region',
            name='mod_date',
        ),
        migrations.AddField(
            model_name='vineyard',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vineyard',
            name='isvalidated',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vineyard',
            name='mod_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]