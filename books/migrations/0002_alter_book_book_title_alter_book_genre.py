# Generated by Django 4.0.4 on 2022-05-02 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=50),
        ),
    ]
