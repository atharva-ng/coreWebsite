# Generated by Django 4.2.7 on 2024-06-07 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_rename_created_event_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='blog',
        ),
    ]