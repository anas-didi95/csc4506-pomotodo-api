from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
  path('todo/', views.ListCreateTodoView.as_view(), name='todo'),
  path('todo/<int:pk>', views.RetrieveUpdateDestroyTodoView.as_view(), name='todo-detail'),
  path('checklist/', views.ListCreateChecklistView.as_view(), name='checklist'),
  path('checklist/<int:pk>', views.RetrieveUpdateDestroyChecklistView.as_view(), name='checklist-detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
