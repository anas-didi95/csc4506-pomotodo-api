from django.test import TestCase
from faker import Faker
from pomotodo.models import Todo, Checklist

class ModelTodoTestCase(TestCase):
  faker = Faker()
  title = faker.sentence()

  def setUp(self):
    self.todo = Todo(title=self.title)
    self.todo.save()

  def testModelTodoCreate(self):
    old_count = Todo.objects.count()
    Todo.objects.create(
      title=self.faker.sentence()
    )
    new_count = Todo.objects.count()
    self.assertNotEqual(old_count, new_count)

  def testModelTodoRetrieve(self):
    todo = Todo.objects.get()
    self.assertEqual(todo.title, self.title)

  def testModelTodoUpdate(self):
    new_title = self.faker.sentence()
    todo = Todo.objects.get(title=self.title)
    Todo.objects.filter(pk=todo.pk).update(
      title=new_title
    )
    todo.refresh_from_db()
    self.assertEqual(todo.title, new_title)

  def testModelTodoDestroy(self):
    old_count = Todo.objects.count()
    Todo.objects.get(title=self.title).delete()
    new_count = Todo.objects.count()
    self.assertNotEqual(old_count, new_count)

class ModelChecklistTestCase(TestCase):
  faker = Faker()
  task = faker.sentence()
  is_done = False

  def setUp(self):
    self.todo = Todo.objects.create(
      title=self.faker.sentence()
    )
    self.checklist = Checklist(
      task=self.task, 
      is_done=self.is_done,
      todo=self.todo
    )
    self.checklist.save()

  def testModelChecklistCreate(self):
    old_count = Checklist.objects.count()
    Checklist.objects.create(
      task=self.faker.sentence(),
      is_done=False,
      todo=self.todo
    )
    new_count = Checklist.objects.count()
    self.assertNotEqual(old_count, new_count)

  def testModelChecklistRetrieve(self):
    checklist = Checklist.objects.get(task=self.task)
    self.assertEqual(checklist.todo.title, self.todo.title)

  def testModelChecklistUpdate(self):
    checklist = Checklist.objects.get(task=self.task)
    Checklist.objects.filter(pk=checklist.pk).update(
      is_done=True
    )
    checklist.refresh_from_db()
    self.assertEqual(checklist.is_done, True)

  def testModelChecklistDestroy(self):
    old_count = Checklist.objects.count()
    Checklist.objects.get(task=self.task).delete()
    new_count = Checklist.objects.count()
    self.assertNotEqual(old_count, new_count)
