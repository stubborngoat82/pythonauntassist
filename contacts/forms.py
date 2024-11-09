from django import forms
from .models import ExternalContact, UserContact

class ExternalContactForm(forms.ModelForm):
    class Meta:
        model = ExternalContact
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'address', 'birthdate', 'notes']

class UserContactForm(forms.ModelForm):
    class Meta:
        model = UserContact
        fields = ['contact_user']
