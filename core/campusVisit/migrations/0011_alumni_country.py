# Generated by Django 4.2.4 on 2024-01-31 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campusVisit', '0010_remove_alumni_comingfrom_alumni_city_alumni_state_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='country',
            field=models.CharField(default='NONE', max_length=100),
        ),
    ]