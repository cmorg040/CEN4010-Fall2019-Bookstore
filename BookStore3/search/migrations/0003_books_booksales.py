# Generated by Django 2.2.5 on 2019-11-20 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20191120_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='bookSales',
            field=models.IntegerField(default=0, verbose_name='Units Sold'),
        ),
    ]
