# Generated by Django 2.2.9 on 2020-01-03 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200103_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 3, 8, 33, 33, 327649)),
        ),
    ]
