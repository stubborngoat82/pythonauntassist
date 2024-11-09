from django.contrib import admin
from .models import ExternalContact, UserContact

@admin.register(ExternalContact)
class ExternalContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email', 'created_at')
    search_fields = ('first_name', 'last_name', 'phone_number', 'email')
    list_filter = ('created_at',)

@admin.register(UserContact)
class UserContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact_user', 'created_at')
    search_fields = ('user__username', 'contact_user__username')
    list_filter = ('created_at',)
