# Generated by Django 3.2.4 on 2021-06-17 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Flights',
            new_name='Flight',
        ),
    ]
