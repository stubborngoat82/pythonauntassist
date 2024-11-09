from django.db import models
from users.models import CustomUser

class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="sent_messages")
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="received_messages")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender} to {self.recipient}"

class CannedMessage(models.Model):
    CATEGORY_CHOICES = [
        ('greeting_goodbye', 'Greetings & Goodbyes'),
        ('health_comfort', 'Health & Comfort'),
        ('assistance', 'Assistance Requests'),
        ('meals_refreshments', 'Meals & Refreshments'),
        ('emotions_social', 'Emotions & Social Interaction'),
        ('schedules_reminders', 'Schedules & Reminders'),
        ('urgent_emergency', 'Urgent/Emergency'),
    ]
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    text = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="canned_messages")

    def __str__(self):
        return f"{self.category} - {self.text[:30]}"
