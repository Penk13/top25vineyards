# Generated by Django 3.2 on 2021-10-07 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_post_body_on_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
    ]
