# Generated by Django 2.1.7 on 2019-04-06 11:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jit', '0003_auto_20190331_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='jit',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='jit',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 6, 11, 31, 1, 995185, tzinfo=utc)),
        ),
    ]
