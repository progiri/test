from django.urls import path

from .views import (
    TaskListCreateAPIView,
    TaskDetailUpdateDeleteAPIView,
)

urlpatterns = [
    path('', TaskListCreateAPIView.as_view(), name='task-list'),
    path('<int:pk>/', TaskDetailUpdateDeleteAPIView.as_view(), name='task-detail')
]
