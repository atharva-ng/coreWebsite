# Generated by Django 4.2.4 on 2024-01-16 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_blog_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='blog',
        ),
        migrations.DeleteModel(
            name='coordi',
        ),
        migrations.DeleteModel(
            name='person',
        ),
    ]