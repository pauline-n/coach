from django import template

from ..models import NavBar

register=template.Library()

@register.simple_tag()
def get_navbar(slug):
    return NavBar.objects.get(slug=slug)