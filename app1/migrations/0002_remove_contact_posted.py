# Generated by Django 4.0.3 on 2022-08-17 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='posted',
        ),
    ]
