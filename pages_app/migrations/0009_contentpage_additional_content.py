# Generated by Django 3.2 on 2021-10-02 02:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0008_alter_imageupload_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentpage',
            name='additional_content',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
