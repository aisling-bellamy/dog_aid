# Generated by Django 2.1.5 on 2020-07-27 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dog_aid', '0012_auto_20200727_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='DogBreed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed_type', models.CharField(blank=True, max_length=128)),
                ('breed_name', models.ForeignKey(max_length=128, null=True, on_delete=django.db.models.deletion.CASCADE, to='dog_aid.DogProfile')),
            ],
        ),
    ]