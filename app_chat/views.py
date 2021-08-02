from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView
import validators
from app_chat.WFTUrls import url_checker
from app_chat.Functions.list_to_text import *
from app_chat.Functions import len_word_checker
from app_chat.Functions.other_functions import *

from app_chat.forms import *
from app_chat.models import *
# Create your views here.


def main_index(request):
    context = {
        'sections':  Section.objects.all(),
    }
    return render(request, 'app_chat/index.html', context=context)

class ChatSection(TemplateView):
    template_name = 'app_chat/chat_her.html'

    def get_context_data(self, **kwargs):
        section_id = kwargs.get('section_id')
        conv = Conversations.objects.filter(section_id=section_id)
        conv_id = self.request.GET.get('conversation')

        if not self.request.user.is_anonymous:
            my_conversations = Conversations.objects.filter(section_id=section_id, user=self.request.user)
        else:
            my_conversations = []

        if conv_id:
            if not self.request.user.is_anonymous:
                my_messages = Message.objects.filter(conversation_id=conv_id, user=self.request.user)
            else:
                my_messages = []
            messages = Message.objects.filter(conversation_id=conv_id)
            conversation_now = Conversations.objects.filter(id=conv_id)
        else:
            messages = []
            my_messages = []
            conversation_now = ""

        mess_r_forms = []
        for i in range(0, len(my_messages)):
            message = MessageRefactorForm()
            message.fields['text'].initial = my_messages[i]
            mess_r_forms.append(message)

        conv_r_forms = []
        for i in range(0, len(my_conversations)):
            conversation = ConversationRefactorForm()
            conversation.fields['text'].initial = my_conversations[i]
            conv_r_forms.append(conversation)

        conv_form = ConversationForm()
        mess_form = MessageForm()

        if 'text' in self.request.POST:
            form_rows = string_counter(self.request.POST['text'])
        else:
            form_rows = 1
        context = super().get_context_data()

        context.update({
        'section_id': section_id,
        'conversations': conv,
        'conversation_now': conversation_now,
        'messages': messages,
        'conversation_id': conv_id,
        'conversation_form': conv_form,
        'message_form': mess_form,
        "message_refactor_forms": mess_r_forms,
        "conversation_refactor_forms": conv_r_forms,
        "section_title":  get_object_or_404(Section, id=section_id).title,
        "m_form_rows": form_rows,
        "c_form_rows": form_rows,
        })

        return context

    def post(self, request, *args, **kwargs):
        user = self.request.user
        section_id = kwargs.get('section_id')
        conv_id = self.request.GET.get('conversation')
        form_type = request.POST.get('form')
        mess_id = request.POST.get('nmd_id')
        conv_now_id = request.POST.get('ncd_id')
        kwargs["message_id"] = mess_id

        if form_type == "conversation":
                conv_form = ConversationForm(request.POST)
                if user.is_anonymous:
                    conv_form.add_error(None, "Вы не вошли в систему !")
                elif conv_form.is_valid():
                    conversation = conv_form.save(commit=False)
                    conversation.section_id = section_id
                    conversation.user = user
                    conversation.save()

        elif form_type == "message":
            if conv_id:
                mess_form = MessageForm(request.POST)
                if user.is_anonymous:
                    mess_form.add_error(None, "Вы не вошли в систему !")
                elif mess_form.is_valid():
                    message = mess_form.save(commit=False)
                    message.conversation_id = conv_id
                    message.user = user
                    if "attached_file" in request.FILES:
                        message.attached_file = request.FILES["attached_file"]

                    if validators.url(message.text) or url_checker.url_her(message.text):
                        message.is_link = True
                        if not validators.url(message.text):
                            result = url_checker.parsing(message.text)
                            message.texts_FIT = translate_ltt(result[0])
                            message.links_FIT = translate_ltt(result[1])

                        else:
                            message.links_FIT = message.text
                            message.texts_FIT = translate_ltt("")
                    else:
                        message.is_link = False
                    message.save()

        elif form_type == "delete":
            Message.objects.filter(id=mess_id).delete()

        elif form_type == "refactor":
            mess_r_form = MessageRefactorForm(request.POST)
            if mess_r_form.is_valid():
                message = mess_r_form.save(commit=False)
                message.conversation_id = conv_id
                message.user = user
                if validators.url(message.text) or url_checker.url_her(message.text):
                    message.is_link = True
                    if not validators.url(message.text):
                        result = url_checker.parsing(message.text)
                        message.texts_FIT = translate_ltt(result[0])
                        message.links_FIT = translate_ltt(result[1])

                    else:
                        message.links_FIT = message.text
                        message.texts_FIT = translate_ltt("")
                else:
                    message.is_link = False
                Message.objects.filter(id=mess_id).update(text=message.text,
                texts_FIT=message.texts_FIT, links_FIT=message.links_FIT, is_link=message.is_link)

        elif form_type == "conversation_delete":
            Conversations.objects.filter(id=conv_now_id).delete()

        elif form_type == "conversation_refactor":
            conv_r_form = ConversationRefactorForm(request.POST)
            if conv_r_form.is_valid():
                conversation = conv_r_form.save(commit=False)
                conversation.section_id = section_id
                conversation.user = user
                Conversations.objects.filter(id=conv_now_id).update(text=conversation.text, )

        return self.get(request, *args, **kwargs)


def notes_chat(request):
    context = {
        'notes':  Note.objects.filter(public=True),
    }
    return render(request, 'app_chat/notes/notes.html', context=context)


def note_create(request):
    if request.POST:
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            note = note_form.save(commit=False)
            note.user = request.user
            if note.name is None:
                note.name = '"Без названия"'
            note.save()
            return redirect(notes_chat)

    context = {
        'note_form': NoteForm()
    }
    return render(request, 'app_chat/notes/create_note.html', context=context)


def profile_notes(request):
    context = {
        'notes': Note.objects.filter(user=request.user),
    }
    return render(request, 'account/my_notes.html', context=context)


def visit_note(request, **kwargs):
    note_id = kwargs.get('note_id')
    if request.POST:
        if request.POST.get('form') == 'refactor':
            note_form = NoteRefactorForm(request.POST)
            if note_form.is_valid():
                note = note_form.save(commit=False)
                note.user = request.user
                note.text = len_word_checker.check_end_return(note.text, mode='note_mode')
                Note.objects.filter(id=note_id).update(text=note.text, )
                return redirect(notes_chat)

        elif request.POST.get('form') == 'delete':
            Note.objects.filter(id=note_id).delete()
            return redirect(notes_chat)

    context = {
        'note': Note.objects.get(id=note_id),
    }
    return render(request, 'app_chat/notes/visit_note.html', context=context)


def visit_text_file(request):
    message_id = int(request.GET.get("message_file"))
    text = "Page blank"
    if message_id:
        file_mess = Message.objects.get(id=message_id)
        text = str(file_mess.attached_file)
        text = open("media/" + text, "r")
        text = text.read()

    return HttpResponse(text)
