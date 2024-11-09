from django import forms
from .models import Message, CannedMessage
from users.models import CustomUser

class MessageForm(forms.ModelForm):
    category = forms.ChoiceField(
        choices=CannedMessage.CATEGORY_CHOICES,
        required=True,
        label="Category"
    )
    canned_message = forms.ModelChoiceField(
        queryset=CannedMessage.objects.none(),  # Start with an empty queryset
        required=False,
        empty_label="Select a canned message"
    )

    class Meta:
        model = Message
        fields = ['recipient', 'category', 'canned_message', 'text']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['recipient'].queryset = CustomUser.objects.exclude(id=user.id)

class CannedMessageForm(forms.ModelForm):
    class Meta:
        model = CannedMessage
        fields = ['category', 'text']