from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.utils.translation import gettext as _, ngettext

@admin.register(User)
class DUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'avatar')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    readonly_fields = ('text', 'user')

@admin.register(Conversations)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'user', 'created_at', 'modified_at')
    list_filter = ('text', 'section')
    search_fields = ('text', 'section__title')
    readonly_fields = ('user', )
    inlines = (MessageInline, )


@admin.register(Message)
class MassageAdmin(admin.ModelAdmin):
    list_display = ('id', 'conversation', 'user', 'created_at', 'modified_at', 'is_link')
    list_filter = ('conversation', 'conversation__section', 'user')
    search_fields = ('text', 'conversation__text', 'conversation__section__title')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'modified_at', 'text')
    list_filter = ('user', )
    search_fields = ('text', 'user')