# Generated by Django 3.2 on 2021-11-10 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vineyards', '0029_reviewandrating_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewandrating',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
