# Generated by Django 2.2.6 on 2019-10-21 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0002_auto_20191014_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humidity',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='pressure',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.DeleteModel(
            name='Time',
        ),
    ]
