# Generated by Django 2.1.7 on 2019-04-11 16:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jit', '0010_auto_20190411_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jit',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 11, 16, 27, 54, 732347, tzinfo=utc)),
        ),
    ]
