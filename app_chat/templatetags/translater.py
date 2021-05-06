from django import template
from app_chat.models import *
from app_chat.Functions.list_to_text import *
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.simple_tag()
def do_tr(value, tl):
    return translate_ttl(value)[tl]


@register.filter
def range_lltt(value):
    return range(len(translate_ttl(value)))
