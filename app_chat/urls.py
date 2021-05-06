from django.urls import path
from app_chat.views import *

urlpatterns = [
    path('', main_index, name="main"),
    path('section/<int:section_id>/', ChatSection.as_view(), name="section"),
    path('section/notes', notes_chat, name="notes_chat"),
]



