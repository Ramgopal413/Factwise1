from rest_framework import serializers
from .models import ProjectBoard

class ProjectBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectBoard
        fields = '__all__'
