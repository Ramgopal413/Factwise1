from django.urls import path
from .views import ProjectBoardListCreateAPIView, ProjectBoardRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', ProjectBoardListCreateAPIView.as_view(), name='project-board-list-create'),
    path('<int:pk>/', ProjectBoardRetrieveUpdateDestroyAPIView.as_view(), name='project-board-retrieve-update-destroy'),
]
