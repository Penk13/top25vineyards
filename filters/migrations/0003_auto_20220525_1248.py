# Generated by Django 3.2 on 2022-05-25 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vineyards', '0062_vineyard_tags'),
        ('filters', '0002_facility_service_wine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='vineyards',
            field=models.ManyToManyField(blank=True, related_name='facility_filter', to='vineyards.Vineyard'),
        ),
        migrations.AlterField(
            model_name='service',
            name='vineyards',
            field=models.ManyToManyField(blank=True, related_name='service_filter', to='vineyards.Vineyard'),
        ),
        migrations.AlterField(
            model_name='wine',
            name='vineyards',
            field=models.ManyToManyField(blank=True, related_name='wine_filter', to='vineyards.Vineyard'),
        ),
        migrations.AlterField(
            model_name='wineregion',
            name='vineyards',
            field=models.ManyToManyField(blank=True, related_name='wineregion_filter', to='vineyards.Vineyard'),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('vineyards', models.ManyToManyField(blank=True, related_name='rating_filter', to='vineyards.Vineyard')),
            ],
        ),
    ]
