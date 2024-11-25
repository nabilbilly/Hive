from django.db import models

# Create your models here.
from typing import Any
from django.db import models
from django.contrib.auth.models import User 
from . import routing

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1,  related_name='teamworkspace_messages')  # assuming user with ID 1 exists
    room = models.CharField(max_length=255, default='general')
    content = models.TextField(default='No content')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.content[:200]}'