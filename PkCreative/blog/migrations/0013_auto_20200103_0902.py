# Generated by Django 2.2.9 on 2020-01-03 09:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200103_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 3, 9, 2, 44, 542775)),
        ),
    ]
