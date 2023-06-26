from rest_framework import generics
from .models import ProjectBoard
from .serializers import ProjectBoardSerializer

class ProjectBoardListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProjectBoard.objects.all()
    serializer_class = ProjectBoardSerializer

class ProjectBoardRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectBoard.objects.all()
    serializer_class = ProjectBoardSerializer
