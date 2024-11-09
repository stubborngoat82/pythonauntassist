from django.urls import path
from . import views

urlpatterns = [
    # ExternalContact URLs
    path('external/', views.external_contact_list, name='external_contact_list'),
    path('external/add/', views.external_contact_create, name='external_contact_create'),
    path('external/edit/<int:pk>/', views.external_contact_update, name='external_contact_update'),
    path('external/delete/<int:pk>/', views.external_contact_delete, name='external_contact_delete'),

    # UserContact URLs
    path('user/', views.user_contact_list, name='user_contact_list'),
    path('user/add/', views.user_contact_create, name='user_contact_create'),
]
