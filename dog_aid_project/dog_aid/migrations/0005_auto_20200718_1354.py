# Generated by Django 2.1.5 on 2020-07-18 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dog_aid', '0004_auto_20200718_1353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='breed',
            new_name='breed_of_dog',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='birth',
            new_name='date_of_birth',
        ),
    ]
