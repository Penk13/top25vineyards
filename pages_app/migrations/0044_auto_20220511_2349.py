# Generated by Django 3.2 on 2022-05-11 16:49

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0032_post_display_cover'),
        ('vineyards', '0061_auto_20220508_1047'),
        ('pages_app', '0043_auto_20220508_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentpage',
            name='additional_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Main Content'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='carousel_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Title Carousel'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='category',
            field=models.ManyToManyField(blank=True, to='vineyards.Region', verbose_name='List Regions'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Header Content'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='content_on_list',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='List Content'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='display_billboard',
            field=models.BooleanField(default=True, verbose_name='Display Billboards'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='display_list',
            field=models.BooleanField(default=True, verbose_name='Display Carousel'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='list_carousel',
            field=models.ManyToManyField(blank=True, related_name='_pages_app_contentpage_list_carousel_+', to='list.Category', verbose_name='List Carousel'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='list_section',
            field=models.ManyToManyField(blank=True, related_name='_pages_app_contentpage_list_section_+', to='list.Category', verbose_name='List Posts'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='listing_title1',
            field=models.CharField(blank=True, max_length=255, verbose_name='Title Region List'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='listing_title2',
            field=models.CharField(blank=True, max_length=255, verbose_name='Title Post List'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='listing_title3',
            field=models.CharField(blank=True, max_length=255, verbose_name='Title Section 3'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='show_listing1',
            field=models.BooleanField(default=False, verbose_name='Display List Regions'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='show_listing2',
            field=models.BooleanField(default=False, verbose_name='Display List Posts'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='show_listing3',
            field=models.BooleanField(default=False, verbose_name='Display List3'),
        ),
    ]
