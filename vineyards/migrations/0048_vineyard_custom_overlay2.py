# Generated by Django 3.2 on 2022-03-24 04:35

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('vineyards', '0047_auto_20220323_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='vineyard',
            name='custom_overlay2',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='custom_overlay2', to=settings.FILER_IMAGE_MODEL),
        ),
    ]
