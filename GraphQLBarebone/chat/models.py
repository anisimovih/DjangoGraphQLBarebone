"""Chat app models."""

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Message(models.Model):
    """Message model."""

    text = models.CharField(max_length=255)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_sent')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_received')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
