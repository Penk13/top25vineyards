# Generated by Django 3.2 on 2021-10-02 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vineyards', '0020_auto_20211001_2217'),
        ('pages_app', '0009_contentpage_additional_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentpage',
            name='category',
            field=models.ManyToManyField(blank=True, to='vineyards.Region'),
        ),
        migrations.AddField(
            model_name='contentpage',
            name='show_listing',
            field=models.BooleanField(default=False),
        ),
    ]
