# Generated by Django 4.2.2 on 2023-06-26 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='population',
        ),
    ]
