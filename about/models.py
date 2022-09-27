from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class About(Page):
    subtitle = models.CharField(max_length=255)
    story = RichTextField()
    picture = models.ForeignKey('wagtailimages.Image', blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
    testimonials = StreamField([
        ('testifier', blocks.StructBlock([
            ('testimony', blocks.RichTextBlock()),
            ('profilepic', ImageChooserBlock()),
            ('name', blocks.CharBlock(form_classname='title')),
            ('profession', blocks.CharBlock(form_classname='title'))
        ]))
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('story'),
        FieldPanel('picture'),
        FieldPanel('testimonials')
    ]

    class Meta:
        verbose_name = 'About Us Page'

    parent_page_types = ['home.HomePage']