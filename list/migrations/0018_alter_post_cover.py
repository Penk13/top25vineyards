# Generated by Django 3.2 on 2021-10-14 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0017_auto_20211013_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, max_length=255, upload_to='list'),
        ),
    ]