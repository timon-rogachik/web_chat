from app_chat.forms import *
from app_chat.models import *
import math

def string_counter(text):
    print(text)
    len_string = len("аааааааааааааааааааааааааааааааааааааааааааааааа")
    if not text == None:
        return int(math.ceil(len(text)/len_string))
    return 1
