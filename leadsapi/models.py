from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from datetime import timezone

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500)
    owner = models.ForeignKey(User, related_name="leads", null=True, on_delete=CASCADE)
    def __str__(self):
        return self.name