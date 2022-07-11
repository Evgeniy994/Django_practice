from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from to_do.models import Task, Tag


def task_change_status(request, pk, action):
    task = Task.objects.get(pk=pk)

    if action == "success":
        task.status = True
    if action == "undo":
        task.status = False

    task.save()

    return HttpResponseRedirect(reverse("to_do:index"))


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "to_do/index.html"
    paginate_by = 10
    ordering = ["status", "-create"]
    queryset = Task.objects.all().prefetch_related("tag")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("to_do:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("to_do:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:task-list")
    template_name = "to_do/task_confirm_delete.html"


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    paginate_by = 10


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do:tag_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do:tag_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "to_do/tag_confirm_delete.html"
    success_url = reverse_lazy("to_do:tag_list")
