# Generated by Django 3.2 on 2022-02-11 05:08

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0024_auto_20220108_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='sidebar',
            field=models.TextField(blank=True),
        ),
    ]
