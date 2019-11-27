# Generated by Django 2.2.6 on 2019-11-05 19:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0020_auto_20191101_0405'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='datePosted',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='comment',
            name='userName',
            field=models.TextField(default='userName'),
        ),
    ]
