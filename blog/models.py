from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]
    parent_page_types=['home.HomePage']

class BlogPage(Page):
    heading = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)
    image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('author'),
        FieldPanel('image'),
        FieldPanel('body')
    ]

    parent_page_types=['home.HomePage']
