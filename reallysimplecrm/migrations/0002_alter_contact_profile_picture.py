# Generated by Django 4.2 on 2023-04-28 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reallysimplecrm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_pictures/default.png', null=True, upload_to='profile_pictures/'),
        ),
    ]
