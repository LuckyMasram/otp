# Generated by Django 4.0 on 2021-12-19 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='mobile',
            new_name='mobile_number',
        ),
    ]