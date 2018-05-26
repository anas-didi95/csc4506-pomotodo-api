from rest_framework import generics
from .serializers import (
  TodoSerializer, TodoDetailSerializer,
  ChecklistSerializer,
)
from .models import Todo, Checklist

class ListCreateTodoView(generics.ListCreateAPIView):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer

class RetrieveUpdateDestroyTodoView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Todo.objects.all()
  serializer_class = TodoDetailSerializer

class ListCreateChecklistView(generics.ListCreateAPIView):
  queryset = Checklist.objects.all()
  serializer_class = ChecklistSerializer

class RetrieveUpdateDestroyChecklistView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Checklist.objects.all()
  serializer_class = ChecklistSerializer