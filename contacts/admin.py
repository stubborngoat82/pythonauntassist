
from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'contact_user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'contact_user__username')
    ordering = ('-created_at',)
    
    def get_queryset(self, request):
        # Customize queryset to reduce duplicate contacts in the admin list
        qs = super().get_queryset(request)
        return qs.distinct()

    def has_add_permission(self, request):
        # Disable adding new Contact instances directly from the admin interface
        return False
