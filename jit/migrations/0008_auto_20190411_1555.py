# Generated by Django 2.1.7 on 2019-04-11 15:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jit', '0007_auto_20190409_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jit',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 11, 15, 55, 59, 730504, tzinfo=utc)),
        ),
    ]