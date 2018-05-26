from rest_framework import serializers
from .models import Todo, Checklist

class TodoSerializer(serializers.ModelSerializer):

  class Meta:
    model = Todo
    fields = (
      'id',
      'title',
    )

class ChecklistSerializer(serializers.ModelSerializer):

  class Meta:
    model = Checklist
    fields = (
      'id',
      'task',
      'is_done',
      'todo',
    )

class TodoDetailSerializer(serializers.ModelSerializer):
  tasks = ChecklistSerializer(many=True, read_only=True)

  class Meta:
    model = Todo
    fields = (
      'id',
      'title',
      'tasks'
    )
