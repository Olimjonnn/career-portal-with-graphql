# Generated by Django 4.2.4 on 2023-08-03 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='tags',
        ),
    ]