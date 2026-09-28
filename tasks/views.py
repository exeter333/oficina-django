from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})


def task_create(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if title:
            priority = int(request.POST.get("priority", 2))
            Task.objects.create(title=title, priority=priority)
        return redirect("task_list")
    return render(request, "tasks/task_form.html")


@require_POST
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect("task_list")


@require_POST
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("task_list")
