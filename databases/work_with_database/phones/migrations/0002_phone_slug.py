# Generated by Django 3.1.2 on 2021-03-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.CharField(default=None, max_length=225),
        ),
    ]
