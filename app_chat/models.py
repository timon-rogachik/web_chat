
from django.db import models
from acounts.models import User


# Create your models here.

class Section(models.Model):
    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to='images/sections', null=True, blank=True)


class Conversations(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="conversation")
    text = models.TextField(max_length=575)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="conversation")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class Message(models.Model):
    conversation = models.ForeignKey(Conversations, on_delete=models.CASCADE, related_name="message")
    text = models.TextField(max_length=1450)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_link = models.BooleanField()
    links_FIT = models.TextField(blank=True, null=True)
    texts_FIT = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.text

    def refactor_text(self, text):
        self.text = text


class Note(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=20, null=True, blank=True, default='"Без названия"')
    public = models.BooleanField(default=True)


