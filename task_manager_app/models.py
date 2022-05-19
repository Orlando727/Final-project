from django.utils import timezone

from django.db import models
from django.urls import reverse

def one_week_task():
    #данная функция возвращает дату выбранную в качетсве послдней даты для завершения задачи
    return timezone.now() + timezone.timedelta(days=7)

class TaskManagerList(models.Model):
    # данный класс служит для создания списка дел, который наследуется из мета класса Джанго
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title

class TaskManagerItem(models.Model):
    # данный класс служит для создания списка задач в списке дле, который наследуется из мета класса Джанго
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_task)
    task_manager_list = models.ForeignKey(TaskManagerList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.task_manager_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: до {self.due_date}"

    class Meta:
        ordering = ["due_date"]
