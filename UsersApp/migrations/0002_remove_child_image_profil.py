# Generated by Django 3.2.5 on 2021-07-12 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='image_profil',
        ),
    ]
