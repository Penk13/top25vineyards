# Generated by Django 3.2 on 2021-09-27 15:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0006_alter_post_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ad_manager',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='sidebar',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]