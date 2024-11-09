from django.db import models
from users.models import CustomUser
# Create your models here.

class Contact(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="contacts")
    contact_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="added_contacts")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact: {self.user.username} -> {self.contact_user.username}"