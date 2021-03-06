# Generated by Django 2.2.9 on 2020-03-06 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('contract', '0005_auto_20200103_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='related_external_url',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='related_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
    ]
