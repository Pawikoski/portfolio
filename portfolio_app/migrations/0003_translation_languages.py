# Generated by Django 4.1.2 on 2022-11-11 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_translation'),
    ]

    operations = [
        migrations.AddField(
            model_name='translation',
            name='languages',
            field=models.CharField(default='Languages', max_length=50),
        ),
    ]
