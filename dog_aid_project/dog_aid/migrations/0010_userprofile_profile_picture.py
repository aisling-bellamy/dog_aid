# Generated by Django 2.1.5 on 2020-07-26 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_aid', '0009_dogprofile_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
    ]
