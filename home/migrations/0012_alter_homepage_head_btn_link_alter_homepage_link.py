# Generated by Django 4.1.1 on 2022-09-28 14:28

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_homepage_blog_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='head_btn_link',
            field=wagtail.fields.RichTextField(default='Free Consultation'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='link',
            field=wagtail.fields.RichTextField(default='Hello world'),
        ),
    ]
