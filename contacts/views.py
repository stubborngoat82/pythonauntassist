from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Contact
from users.models import CustomUser

class ContactListView(ListView):
    model = Contact
    template_name = 'contacts/contact_list.html'
    context_object_name = 'contacts'

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)

class ContactCreateView(CreateView):
    model = Contact
    fields = ['contact_user']
    template_name = 'contacts/contact_form.html'
    success_url = reverse_lazy('contact_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)