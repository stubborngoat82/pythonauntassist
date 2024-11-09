from django.shortcuts import render
from typing import Dict, Any
from django.urls import reverse_lazy
from django.views import View
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Message, CannedMessage
from users.models import CustomUser
from .forms import MessageForm, CannedMessageForm

class MessageListView(ListView):
    model = Message
    template_name = 'messaging/message_list.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return Message.objects.filter(recipient=self.request.user)

class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'messaging/message_form.html'
    success_url = reverse_lazy('message_list')

    def get_form_kwargs(self) -> Dict[str, Any]:
        kwargs =  super().get_form_kwargs()
        kwargs['user']= self.request.user
        return kwargs


    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)
    

class CannedMessageCreateView(LoginRequiredMixin, CreateView):
    model = CannedMessage
    form_class = CannedMessageForm
    template_name = 'messaging/canned_message_form.html'
    success_url = reverse_lazy('canned_message_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CannedMessageListView(View):
    def get(self, request, category):
        messages = CannedMessage.objects.filter(category=category)
        data = [{'id': message.id, 'text': message.text[:50]} for message in messages]
        return JsonResponse(data, safe=False)
        model = CannedMessage
    form_class = CannedMessageForm
    template_name = 'messaging/canned_message_form.html'
    success_url = reverse_lazy('canned_message_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class CannedMessageUpdateView(LoginRequiredMixin, UpdateView):
    model = CannedMessage
    form_class = CannedMessageForm
    template_name = 'messaging/canned_message_form.html'
    success_url = reverse_lazy('canned_message_list')

    def get_queryset(self):
        return CannedMessage.objects.filter(created_by=self.request.user)

class CannedMessageDeleteView(LoginRequiredMixin, DeleteView):
    model = CannedMessage
    template_name = 'messaging/canned_message_confirm_delete.html'
    success_url = reverse_lazy('canned_message_list')

    def get_queryset(self):
        return CannedMessage.objects.filter(created_by=self.request.user)