from django.db import models

class Todo(models.Model):
  title = models.CharField()