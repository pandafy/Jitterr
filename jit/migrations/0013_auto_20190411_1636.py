# Generated by Django 2.1.7 on 2019-04-11 16:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jit', '0012_auto_20190411_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jit',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 11, 16, 36, 53, 934156, tzinfo=utc)),
        ),
    ]