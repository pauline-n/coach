from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PageChooserPanel, InlinePanel
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks
from wagtail.models import Page, Orderable

class HomePage(Page):
    b_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    head_msg = models.CharField(max_length=200, default='Vincent')
    head_body = RichTextField(default='Hello world')
    head_btn_link = RichTextField(default='Free Consultation')
    pic = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    info = RichTextField(default='Hello world')
    link = RichTextField(default='Hello world')
    team = StreamField([
        ('teammate', blocks.StructBlock([
            ('photo', ImageChooserBlock()),
            ('name', blocks.CharBlock(form_classname="title")),
            ('details', blocks.CharBlock(form_classname="title")),
        ]))
       
    ], use_json_field=True, blank=True)

    contact_phone = models.CharField(max_length=200, default ='256774559687')
    contact_email = models.EmailField(default='ojaravincent5@gmail.com')
    contact_location = models.CharField(max_length=255, default='Kampala, Uganda')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('b_image'),
            FieldPanel('head_msg'),
            FieldPanel('head_body'),
            FieldPanel('head_btn_link'),
        ], heading='Home header section' ),
        InlinePanel('our_services', label='Services', min_num=1, max_num=6),
        MultiFieldPanel([
            FieldPanel('pic'),
            FieldPanel('info'),
            FieldPanel('link')
        ], heading='Brief information about us'),
        InlinePanel('our_prices', label='Pricing', max_num=3, min_num=1),
        FieldPanel('team'),
        # PageChooserPanel('blog_feature'),
        MultiFieldPanel([
            FieldPanel('contact_phone'),
            FieldPanel('contact_email'),
            FieldPanel('contact_location'),
        ])
    ]

    class Meta:
        verbose_name = 'Home Page'


class HomePagePrices(Orderable):
    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='our_prices')
    price_type = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    basis = models.CharField(max_length=200)
    breakdown = RichTextField()
    order_link = models.CharField(max_length=200)

    panels = [
        FieldPanel('price_type'),
        FieldPanel('price'),
        FieldPanel('basis'),
        FieldPanel('breakdown'),
        FieldPanel('order_link'),
    ]

class HomePageServices(Orderable):
    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='our_services')
    icon = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    service = models.CharField(max_length=200, blank=True)
    description = RichTextField(default='Hello world')

    panels = [
        FieldPanel('icon'),
        FieldPanel('service'),
        FieldPanel('description'),
    ]
