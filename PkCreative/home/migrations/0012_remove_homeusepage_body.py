# Generated by Django 2.2.9 on 2020-03-09 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20200228_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeusepage',
            name='body',
        ),
    ]
