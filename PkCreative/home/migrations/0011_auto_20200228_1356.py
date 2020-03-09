# Generated by Django 2.2.9 on 2020-02-28 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_homepage_banner_cta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='banner_cta',
            new_name='related_page',
        ),
        migrations.RenameField(
            model_name='homeusepage',
            old_name='banner_cta',
            new_name='related_page',
        ),
        migrations.AddField(
            model_name='homepage',
            name='related_external_url',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AddField(
            model_name='homeusepage',
            name='related_external_url',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
    ]