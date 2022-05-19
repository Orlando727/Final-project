
from django.urls import reverse, reverse_lazy

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    
)
from .models import TaskManagerList, TaskManagerItem

class ListListView(ListView):
    model = TaskManagerList
    template_name = "task_manager_app/index.html"

class ItemListView(ListView):
    model = TaskManagerItem
    template_name = "task_manager_app/task_manager_list.html"

    def get_queryset(self):
        return TaskManagerItem.objects.filter(task_manager_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["task_manager_list"] = TaskManagerList.objects.get(id=self.kwargs["list_id"])
        return context

class ListCreate(CreateView):
    model = TaskManagerList
    fields = ["title"]

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Добавьте новое задание"
        return context

class ItemCreate(CreateView):
    model = TaskManagerItem
    fields = [
        "task_manager_list",
        "title",
        "description",
        "due_date",
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        task_manager_list = TaskManagerList.objects.get(id=self.kwargs["list_id"])
        initial_data["task_manager_list"] = task_manager_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        task_manager_list = TaskManagerList.objects.get(id=self.kwargs["list_id"])
        context["task_manager_list"] = task_manager_list
        context["title"] = "Создание нового задания"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.task_manager_list_id])

class ItemUpdate(UpdateView):
    model = TaskManagerItem
    fields = [
        "task_manager_list",
        "title",
        "description",
        "due_date",
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["task_manager_list"] = self.object.task_manager_list
        context["title"] = "Изменить задачу"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.task_manager_list_id])

class ListDelete(DeleteView):
    model = TaskManagerList
    # You have to use reverse_lazy() instead of reverse(),
    # as the urls are not loaded when the file is imported.
    success_url = reverse_lazy("index")

class ItemDelete(DeleteView):
    model = TaskManagerItem

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_manager_list"] = self.object.task_manager_list
        return context


