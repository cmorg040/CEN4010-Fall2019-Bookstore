# Generated by Django 2.2.7 on 2019-11-16 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0024_review_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='nickname',
            field=models.BooleanField(default=False),
        ),
    ]