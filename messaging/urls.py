from django.urls import path
from .views import MessageListView, MessageCreateView, CannedMessageListView, CannedMessageDeleteView, CannedMessageCreateView, CannedMessageUpdateView

urlpatterns = [
    path('', MessageListView.as_view(), name='message_list'),
    path('send/', MessageCreateView.as_view(), name='message_send'),
    path('canned/', CannedMessageListView.as_view(), name='canned_message_list'),
    path('canned/add/', CannedMessageCreateView.as_view(), name='canned_message_add'),
    path('canned/edit/<int:pk>/', CannedMessageUpdateView.as_view(), name='canned_message_edit'),
    path('canned/delete/<int:pk>/', CannedMessageDeleteView.as_view(), name='canned_message_delete'),
]