from django.db import models
from django_extensions.db.fields import AutoSlugField

from wagtail.models import Orderable
from wagtail.admin.panels import FieldPanel, PageChooserPanel, InlinePanel, MultiFieldPanel
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.snippets.models import register_snippet


class NavItems(Orderable):
    page = ParentalKey('navigation.NavBar', on_delete=models.CASCADE, related_name='nav_items')

    page_title = models.CharField(max_length=50, blank=True, null=True)
    page_url = models.CharField(max_length=50, blank=True, null=True)
    link_to_page = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    open_next_tab = models.BooleanField()

    panels = [
        FieldPanel('page_title'),
        FieldPanel('page_url'),
        PageChooserPanel('link_to_page'),
        FieldPanel('open_next_tab'),
    ]
@register_snippet
class NavBar(ClusterableModel):
    name = models.CharField(max_length=100, blank=True, null=True)
    slug = AutoSlugField(populate_from='name', editable=True)

    panels = [
        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('slug')
        ], heading = 'Menu'),
        InlinePanel('nav_items')
    ]

    def __str__(self):
        return self.name

    @property
    def link(self):
        if self.page_url:
            return self.page_url
        elif self.link_to_page:
            return self.link_to_page.url
        else:
            return '#'

    @property 
    def nav_title(self):
        if self.link_to_page and not self.page_title:
            return self.link_to_page.title
        elif self.page_title:
            return self.page_title
        return 'Missing'
