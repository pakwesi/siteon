# Generated by Django 2.2.9 on 2020-01-03 09:02

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtailstreamforms.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailmenus', '0023_remove_use_specific'),
        ('contract', '0002_basicpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formfield',
            name='page',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='from_address',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='to_address',
        ),
        migrations.AddField(
            model_name='contactpage',
            name='body',
            field=wagtail.core.fields.StreamField([('form', wagtail.core.blocks.StructBlock([('form', wagtailstreamforms.blocks.FormChooserBlock()), ('form_action', wagtail.core.blocks.CharBlock(help_text='The form post action. "" or "." for the current page or a url', required=False)), ('form_reference', wagtailstreamforms.blocks.InfoBlock(help_text='This form will be given a unique reference once saved', required=False))]))], blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='BasicPage',
        ),
        migrations.DeleteModel(
            name='FormField',
        ),
    ]