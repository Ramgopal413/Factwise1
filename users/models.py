from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # Add any additional fields you need for the user model

def __str__(self):
    return self.name