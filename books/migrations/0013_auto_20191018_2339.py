# Generated by Django 2.2.6 on 2019-10-18 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_auto_20191018_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='publisherDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
