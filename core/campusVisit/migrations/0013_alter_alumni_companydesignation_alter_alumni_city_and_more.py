# Generated by Django 4.2.4 on 2024-02-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campusVisit', '0012_rename_relatedalumni_guest_visitrequestform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='CompanyDesignation',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='country',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='currAddress',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='currCompany',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='state',
            field=models.CharField(max_length=100),
        ),
    ]
