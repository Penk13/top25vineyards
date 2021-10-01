# Generated by Django 3.2 on 2021-10-01 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vineyards', '0015_auto_20211001_0829'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='YardCoverImage',
            new_name='CoverSliderImage',
        ),
        migrations.RenameModel(
            old_name='YardImage',
            new_name='TopSliderImage',
        ),
        migrations.RenameField(
            model_name='vineyard',
            old_name='under_review',
            new_name='hide_rating',
        ),
        migrations.AddField(
            model_name='vineyard',
            name='custom_overlay',
            field=models.ImageField(blank=True, upload_to='custom-rating/'),
        ),
        migrations.AlterField(
            model_name='region',
            name='logo_on_navbar',
            field=models.ImageField(blank=True, upload_to='logo-on-navbar/'),
        ),
    ]
