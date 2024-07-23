from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer

from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .documents import TaskDocument
from .serializers import TaskSerializer
# Create your views here.

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes=[IsAuthenticated]
    

class TaskDocumentView(DocumentViewSet):
    document = TaskDocument
    serializer_class = TaskSerializer
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
    ]
    search_fields = (
        'title',
        'description',
    )
    filter_fields = {
        'priority': 'priority',
        'due_date': 'due_date',
    }
    ordering_fields = {
        'title': 'title',
        'due_date': 'due_date',
    }


    ordering = ('due_date',)