from django import template
# noinspection PyUnresolvedReferences
from mayphat.models import Setting, Slide, Post

# noinspection PyUnresolvedReferences


register = template.Library()


@register.simple_tag
def get_setting():
    infor = Setting.objects.all()
    for x in infor:
        values = x
    return values


@register.simple_tag
def get_slide():
    infor = Slide.objects.all().filter(status='Slide')

    return infor

