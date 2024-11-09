from django.db import models
from django.conf import settings
from users.models import CustomUser


class ExternalContact(models.Model):
    user = models.ForeignKey(
      CustomUser,
        on_delete=models.CASCADE,
        related_name='contacts'
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # Add any additional fields you need.

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class UserContact(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_contacts")
    contact_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="added_by")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact: {self.user.username} -> {self.contact_user.username}"