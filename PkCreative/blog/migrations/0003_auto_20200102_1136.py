# Generated by Django 2.2.9 on 2020-01-02 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogdetailpage_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 2, 11, 35, 50, 368337)),
        ),
    ]
