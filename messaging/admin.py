from django.contrib import admin
from .models import Message, CannedMessage

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'recipient', 'created_at', 'is_read', 'text_excerpt')
    list_filter = ('is_read', 'created_at')
    search_fields = ('sender__username', 'recipient__username', 'text')
    ordering = ('-created_at',)

    def text_excerpt(self, obj):
        return obj.text[:50] + "..." if len(obj.text) > 50 else obj.text
    text_excerpt.short_description = 'Message Preview'

@admin.register(CannedMessage)
class CannedMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'text_excerpt', 'created_by')
    list_filter = ('category',)
    search_fields = ('text', 'created_by__username')
    ordering = ('category',)

    def text_excerpt(self, obj):
        return obj.text[:50] + "..." if len(obj.text) > 50 else obj.text
    text_excerpt.short_description = 'Canned Message Preview'
