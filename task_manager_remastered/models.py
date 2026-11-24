from django.db import models
from django.contrib.auth.models import User

class ConfirmEmail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)

class Task(models.Model):
    name = models.CharField(max_length=120)
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
