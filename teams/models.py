from django.db import models
from users.models import User
class Team(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=128)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add any additional fields you need for the team model

def __str__(self):
    return self.name