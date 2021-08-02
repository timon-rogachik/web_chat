from django import template
from app_chat.models import *
from app_chat.Functions.list_to_text import *
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag()
def printline(string):
    print("line: ", string)

@register.simple_tag()
def user_check(user, messages):
    result = []
    for i in messages:
        if i.user == user:
            result.append(i)
    return result

@register.simple_tag()
def get_value_by_element(sam_list, element):
    if not element >= len(list(sam_list)):
        return sam_list[element]

@register.simple_tag()
def find_element(list1, value, list2):
    corect_list = list(list1)
    for i in range(0, len(corect_list)):
        result = str(corect_list[i]).replace('<Message:', "")
        corect_list[i] = result.replace('>', "")
    result = 0
    for i in range(0, len(corect_list)):
        if corect_list[i] == value:
            result = i
    return result

@register.simple_tag()
def user_sorted(messages, user):
    return messages.objects.filter(user=user)


@register.simple_tag()
def refactor_id(id):
    return "refactor"+str(id)+'m'


@register.simple_tag()
def refactor_form_id(id):
    return "refactor"+str(id)+"form"+'m'

@register.simple_tag()
def div_id(id):
    return "div"+str(id)+'m'


@register.simple_tag()
def refactor_btn(id):
    return "r-btn"+str(id)+'m'

@register.simple_tag()
def conv_refactor_id(id):
    return "refactor"+str(id)+'c'


@register.simple_tag()
def conv_refactor_form_id(id):
    return "refactor"+str(id)+"form"+'c'

@register.simple_tag()
def conv_div_id(id):
    return "div"+str(id)+'c'


@register.simple_tag()
def conv_refactor_btn(id):
    return "r-btn"+str(id)+'c'


@register.simple_tag()
def t_conversation_id(id):
    return "conversation"+str(id)

@register.simple_tag()
def max_form_width():
    return int(len("25 апреля 2021 г. 13:42 - это :")* 11.5)


@register.simple_tag()
def return_my(conversation_id, messages, user=None):
    if user == None:
        return messages.objects.filter(conversation_id=conversation_id)

    return messages.objects.filter(conversation_id=conversation_id, user=user)


@register.simple_tag()
def get_text_from_form(form):
    return form.fields['text']


@register.simple_tag()
def get_value_by_element(sam_list, element):
    return(sam_list[element])
