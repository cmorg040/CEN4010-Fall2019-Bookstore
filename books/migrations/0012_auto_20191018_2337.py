# Generated by Django 2.2.6 on 2019-10-18 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_books_booksummary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='publisherDate',
            field=models.DateField(default=0.0005025125628140704),
        ),
    ]
