# Generated by Django 3.2 on 2021-09-30 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vineyards', '0012_yardcoverimage_yardimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='vineyard',
            name='region_child',
            field=models.ManyToManyField(blank=True, to='vineyards.RegionChild'),
        ),
    ]
