# Generated by Django 4.1.1 on 2022-09-23 05:27

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_homepageprices_heading'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='details',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='name',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='photo',
        ),
        migrations.AddField(
            model_name='homepage',
            name='team',
            field=wagtail.fields.StreamField([('photo', wagtail.images.blocks.ImageChooserBlock()), ('name', wagtail.blocks.CharBlock(form_classname='title')), ('details', wagtail.blocks.CharBlock(form_classname='title'))], blank=True, use_json_field=True),
        ),
    ]