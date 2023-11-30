# Generated by Django 4.2.7 on 2023-11-30 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='campusVisitRequest',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('studentId', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.IntegerField()),
                ('reason', models.CharField(max_length=254)),
                ('datesFrom', models.DateTimeField()),
                ('datesTo', models.DateTimeField()),
            ],
        ),
    ]
