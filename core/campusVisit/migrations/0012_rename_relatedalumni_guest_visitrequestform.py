# Generated by Django 4.2.4 on 2024-02-06 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusVisit', '0011_alumni_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='relatedAlumni',
            new_name='visitRequestForm',
        ),
    ]