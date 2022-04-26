# Generated by Django 3.2 on 2022-04-12 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vineyards', '0052_auto_20220406_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='vineyard',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='vineyard',
            name='email1',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='vineyard',
            name='email2',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='vineyard',
            name='number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='vineyard',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vineyard',
            name='web_text',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='vineyard',
            name='website',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]