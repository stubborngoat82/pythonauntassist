from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    USER_ROLES = (
        ('admin', 'Administrator'),
        ('patient', 'Patient'),
        ('caregiver', 'Caregiver'),
        ('family', 'Family Member'),
        ('friend', 'Friend')
    )
    
    role = models.CharField(max_length=20, choices=USER_ROLES, default='family')
   

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    emergency_contact = models.CharField(max_length=100, blank=True)
    emergency_phone = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"