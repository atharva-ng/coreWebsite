# Generated by Django 4.2.7 on 2024-01-05 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusVisit', '0005_rename_alumini_alumni'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='relatedAlumini',
            new_name='relatedAlumni',
        ),
        migrations.RemoveField(
            model_name='alumni',
            name='arrivialDate',
        ),
    ]
