# Generated by Django 3.2.5 on 2021-08-08 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='image_badge',
            field=models.ImageField(blank=True, default='ex-par-nat_logo.png', null=True, upload_to='badge_image/'),
        ),
    ]
