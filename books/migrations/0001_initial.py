# Generated by Django 4.0.4 on 2022-05-01 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=60)),
                ('author', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=20)),
                ('publised', models.IntegerField()),
                ('book_length', models.IntegerField()),
            ],
        ),
    ]