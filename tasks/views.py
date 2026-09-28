from django.shortcuts import redirect, render

from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})


def task_create(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if title:
            Task.objects.create(title=title)
        return redirect("task_list")
    return render(request, "tasks/task_form.html")
