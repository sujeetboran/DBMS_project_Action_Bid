# Generated by Django 3.0.6 on 2020-08-01 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='end_interval',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='start_interval',
            field=models.DateField(),
        ),
    ]