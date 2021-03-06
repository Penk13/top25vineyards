# Generated by Django 3.2 on 2022-05-04 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0036_alter_contentpage_types'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contentpage',
            old_name='news',
            new_name='list',
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='types',
            field=models.CharField(choices=[('PAGE', 'Page'), ('FOOTER', 'Footer'), ('HOME_PAGE', 'Home Page'), ('SEARCH_PAGE', 'Search Page'), ('CATEGORY', 'Category'), ('WITHOUT_SIDEBAR', 'Without Sidebar'), ('ARTICLES', 'Articles')], max_length=20),
        ),
    ]
