from django.urls import path

from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("nova/", views.task_create, name="task_create"),
    path("<int:pk>/concluir/", views.task_toggle, name="task_toggle"),
    path("<int:pk>/apagar/", views.task_delete, name="task_delete"),
]
