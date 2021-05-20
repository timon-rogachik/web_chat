from django.urls import path
from app_chat.views import *

urlpatterns = [
    path('', main_index, name="main"),
    path('section/<int:section_id>/', ChatSection.as_view(), name="section"),
    path('section/notes/', notes_chat, name="notes_chat"),
    path('section/notes/create_new/', note_create, name="notes_form"),
    path('profile/notes/', profile_notes, name="profile_notes"),
    path('section/notes/visit/<int:note_id>/', visit_note, name="visit_note"),
]



