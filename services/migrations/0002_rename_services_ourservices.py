# Generated by Django 4.1.1 on 2022-09-27 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('wagtailcore', '0077_alter_revision_user'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Services',
            new_name='OurServices',
        ),
    ]