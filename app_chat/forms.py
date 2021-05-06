from django import forms
from app_chat.models import *


class ConversationForm(forms.ModelForm):
    class Meta:
        model = Conversations
        fields = ("text", )


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("text", "is_link")


class MessageRefactorForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("text", )


class ConversationRefactorForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("text", )