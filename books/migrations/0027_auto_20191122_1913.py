# Generated by Django 2.2.5 on 2019-11-23 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0026_auto_20191120_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='bookRating',
            field=models.IntegerField(default='1'),
        ),
    ]
