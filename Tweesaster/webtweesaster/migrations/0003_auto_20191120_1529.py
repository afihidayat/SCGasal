# Generated by Django 2.1.1 on 2019-11-20 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtweesaster', '0002_profile_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favorites',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='retweets',
            field=models.TextField(),
        ),
    ]
