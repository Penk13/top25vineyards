# Generated by Django 3.2 on 2021-10-24 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vineyards', '0025_auto_20211024_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewandrating',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
