from django.urls import path
from .views import TeamListCreateAPIView, TeamRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', TeamListCreateAPIView.as_view(), name='team-list-create'),
    path('<int:pk>/', TeamRetrieveUpdateDestroyAPIView.as_view(), name='team-retrieve-update-destroy'),
]
