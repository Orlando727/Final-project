from django.contrib import admin
from task_manager_app.models import TaskManagerItem, TaskManagerList

admin.site.register(TaskManagerItem)
admin.site.register(TaskManagerList)
