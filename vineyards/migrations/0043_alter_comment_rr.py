# Generated by Django 3.2 on 2022-03-10 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vineyards', '0042_auto_20220310_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vineyards.reviewandrating'),
        ),
    ]
