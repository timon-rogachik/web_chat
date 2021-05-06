from django import template
import math
from app_chat.models import *
from app_chat.Functions.list_to_text import *
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def max_string_len(text):
    if len(text) >= len("ааааааааааааааааааааааааааааааааааааааааа"):
        return len("ааааааааааааааааааааааааааааааааааааааааа") * 14
    elif len(text) >= len("19 апреля 2021 г. 7:19"):
        return int(len(text) * 11.5)
    else:
        return 245

@register.filter
def max_string_len_cnv(text):
    if len(text) >= len("ааааааааааааааааааааааааааааааааааааа"):
        return len("ааааааааааааааааааааааааааааааааааааа") * 15
    elif len(text) >= len("19 апреля 2021 г. 7:19"):
        return int(len(text) * 12.2)
    else:
        return 260


@register.filter
def min_width_text(text):
    return len(text)*30


@register.filter
def MARGIN(value):
    return 500 - value


@register.filter
def len_check_cut(word):
    if not len(word) <= 0:
        if len(word[0].text) > len('Тимур, прочитай книжку!'):
            result = ''
            for i in range(0, len(word[0].text)):
                if i > len('Тимур, прочитай книжку!'):
                    return result+"..."
                else:
                    result += word[0].text[i]
        return word[0]

    else: return ' '


@register.filter
def string_counter(text):
    print(text)
    len_string = len("аааааааааааааааааааааааааааааааааааааааааааааааа")
    return int(math.ceil(len(text)/len_string))