# Generated by Django 3.2 on 2022-05-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0028_auto_20220507_2028'),
        ('pages_app', '0037_auto_20220504_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentpage',
            name='list',
        ),
        migrations.AddField(
            model_name='contentpage',
            name='list_carousel',
            field=models.ManyToManyField(blank=True, related_name='_pages_app_contentpage_list_carousel_+', to='list.Category'),
        ),
        migrations.AddField(
            model_name='contentpage',
            name='list_section',
            field=models.ManyToManyField(blank=True, related_name='_pages_app_contentpage_list_section_+', to='list.Category'),
        ),
    ]