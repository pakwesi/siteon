# Generated by Django 2.2.9 on 2020-01-02 21:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200102_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 2, 21, 8, 38, 476618)),
        ),
    ]