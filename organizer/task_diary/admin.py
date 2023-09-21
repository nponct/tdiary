from django.contrib import admin
from .import models



@admin.register(models.Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display=('id','title','user','created','datecompleted','memo','is_deleted')
    list_display_links=('title',)
