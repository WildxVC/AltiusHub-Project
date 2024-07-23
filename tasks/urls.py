from django.urls import path
from .views import TaskListCreateView,TaskDetailView,TaskDocumentView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(),name='tast-list-create'),
    path('tasks/<int:pk>', TaskDetailView.as_view(),name='task-detail'),
    path('search/', TaskDocumentView.as_view({'get':'list'}),name='task-search'),
]
