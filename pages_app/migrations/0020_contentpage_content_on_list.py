# Generated by Django 3.2 on 2021-10-07 08:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0019_contentpage_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentpage',
            name='content_on_list',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
