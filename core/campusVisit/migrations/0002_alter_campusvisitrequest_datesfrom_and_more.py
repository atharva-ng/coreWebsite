# Generated by Django 4.2.7 on 2023-11-30 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campusVisit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campusvisitrequest',
            name='datesFrom',
            field=models.DateField(verbose_name='From Date'),
        ),
        migrations.AlterField(
            model_name='campusvisitrequest',
            name='datesTo',
            field=models.DateField(verbose_name='To Date'),
        ),
    ]
