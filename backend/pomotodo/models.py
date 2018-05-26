from django.db import models

class Todo(models.Model):
  title = models.CharField(max_length=255)

  def __str__(self):
    return "%s" % (self.title)

class Checklist(models.Model):
  task = models.CharField(max_length=255)
  is_done = models.BooleanField(default=False)
  todo = models.ForeignKey(
    'Todo',
    on_delete=models.CASCADE,
    related_name='tasks'
  )