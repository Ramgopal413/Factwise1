from django.db import models
from teams.models import Team


class ProjectBoard(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    # Add any additional fields you need for the board model
def __str__(self):
    return self.name