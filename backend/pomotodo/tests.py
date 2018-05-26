from django.test import TestCase
from faker import Faker

class ModelTestCase(TestCase):
  faker = Faker()
  title = faker.sentence()

  def setUp(self):
    self.todo = Todo(title=self.title)

  def testModelTodoCreate(self):
    old_count = Todo.objects.count()
    self.todo.save()
    new_count = Todo.objects.count()
    self.assertNotEqual(old_count, new_count)