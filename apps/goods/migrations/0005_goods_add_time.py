# Generated by Django 2.0.6 on 2018-06-24 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_remove_goods_add_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 24, 17, 25, 20, 321904)),
        ),
    ]
