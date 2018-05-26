from django.contrib import admin
from .models import Todo, Checklist

class ChecklistInline(admin.TabularInline):
  model = Checklist

class TodoAdmin(admin.ModelAdmin):
  list_display = ('title', 'ongoing', 'completed')
  search_fields = ['title',]
  inlines = [ChecklistInline,]

  def completed(self, obj):
    return obj.tasks.filter(is_done=True).count()

  def ongoing(self, obj):
    return obj.tasks.filter(is_done=False).count()

class ChecklistAdmin(admin.ModelAdmin):
  list_display = ('task', 'is_done')
  list_filter = ('is_done', 'todo__title')

admin.site.register(Todo, TodoAdmin)
admin.site.register(Checklist, ChecklistAdmin)