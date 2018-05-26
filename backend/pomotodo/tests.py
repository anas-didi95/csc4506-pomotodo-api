from django.test import TestCase
from faker import Faker
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
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

class ViewTodoTestCase(APITestCase):
  faker = Faker()
  title = faker.sentence()
  clien = APIClient()

  def setUp(self):
    self.todo_data = {'title': self.title}
    self.response = self.client.post(
      reverse('todo'),
      self.todo_data,
      format='json'
    )

  def testViewTodoCreate(self):
   self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

  def testViewTodoRetrieve(self):
    todo = Todo.objects.get(title=self.title)
    response = self.client.get(
      reverse('todo-detail', kwargs={'pk':todo.pk}),
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def testViewTodoUpdate(self):
    todo = Todo.objects.get(title=self.title)
    todo_new_data = {'title':self.faker.sentence()}
    response = self.client.put(
      reverse('todo-detail', kwargs={'pk':todo.pk}),
      todo_new_data,
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertContains(response, todo_new_data['title'])

  def testViewTodoUpdate(self):
    todo = Todo.objects.get(title=self.title)
    response = self.client.delete(
      reverse('todo-detail', kwargs={'pk':todo.pk}),
      format='json'
    )
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ViewChecklistTestCase(APITestCase):
  faker = Faker()
  task = faker.sentence()
  is_done = False

  def setUp(self):
    self.todo = Todo.objects.create(title=self.faker.sentence())
    self.checklist_data = {'task':self.task,'is_done':self.is_done,'todo':self.todo.pk}
    self.response = self.client.post(
      reverse('checklist'),
      self.checklist_data,
      format='json'
    )

  def testViewChecklistCreate(self):
    self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

  def testViewChecklistRetrieve(self):
    checklist = Checklist.objects.get(task=self.task)
    response = self.client.get(
      reverse('checklist-detail', kwargs={'pk':checklist.pk}),
      format='json',
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def testViewChecklistUpdate(self):
    checklist = Checklist.objects.get(task=self.task)
    checklist_new_data = {'task':self.faker.sentence(), 'is_done':checklist.is_done, 'todo':checklist.todo.pk}
    response = self.client.put(
      reverse('checklist-detail', kwargs={'pk':checklist.pk}),
      checklist_new_data,
      format='json',
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertContains(response, checklist_new_data['task'])

  def testViewChecklistDestroy(self):
    checklist = Checklist.objects.get(task=self.task)
    response = self.client.delete(
      reverse('checklist-detail', kwargs={'pk':checklist.pk}),
      format='json',
    )
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)