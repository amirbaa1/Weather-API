# Generated by Django 4.2 on 2023-07-11 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WeatherModel',
            new_name='City',
        ),
    ]
