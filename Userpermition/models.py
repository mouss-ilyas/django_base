# myapp/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLES = (
        ('ADMIN', 'Admin'),
        ('EDITOR', 'Editor'),
        ('VIEWER', 'Viewer'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='VIEWER')

    def __str__(self):
        return self.username
