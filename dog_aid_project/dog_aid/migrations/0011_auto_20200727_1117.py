# Generated by Django 2.1.5 on 2020-07-27 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dog_aid', '0010_userprofile_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile_picture',
            new_name='picture',
        ),
    ]