from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField

class OurServicesIndex(Page):
    intro = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]
class OurServices(Page):
    service_name = models.CharField(max_length=255)
    cover_image = models.ForeignKey('wagtailimages.Image', blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
    content = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('service_name'),
        FieldPanel('cover_image'),
        FieldPanel('content'),

    ]

    class Meta:
        verbose_name = 'Our services'

    parent_page_types=['home.HomePage']

