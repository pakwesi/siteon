# Generated by Django 2.2.9 on 2020-01-03 07:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200102_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 3, 7, 45, 26, 657921)),
        ),
    ]
