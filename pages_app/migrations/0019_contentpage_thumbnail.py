# Generated by Django 3.2 on 2021-10-07 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0018_alter_contentpage_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentpage',
            name='thumbnail',
            field=models.ImageField(blank=True, max_length=255, upload_to='thumbnail-page/'),
        ),
    ]
