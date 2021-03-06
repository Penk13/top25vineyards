# Generated by Django 3.2 on 2022-05-16 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vineyards', '0061_auto_20220508_1047'),
        ('filters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('vineyards', models.ManyToManyField(blank=True, to='vineyards.Vineyard')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('vineyards', models.ManyToManyField(blank=True, to='vineyards.Vineyard')),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('vineyards', models.ManyToManyField(blank=True, to='vineyards.Vineyard')),
            ],
        ),
    ]
