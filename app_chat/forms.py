from django import forms
from app_chat.models import *


class ConversationForm(forms.ModelForm):
    class Meta:
        model = Conversations
        fields = ("text", )


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("text", "attached_file", )


class MessageRefactorForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("text", )


class ConversationRefactorForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("text", )


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("text", "name", "public", )


class NoteRefactorForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("text", )