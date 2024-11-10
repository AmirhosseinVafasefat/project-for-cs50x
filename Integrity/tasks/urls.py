from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name = "index"),
    path("remove_task/<int:task_id>", views.remove_task, name = "remove_task"), 
    path("edit_task/<int:task_id>", views.edit_task, name = "edit_task"),
    path("add_subtask/<int:task_id>", views.add_subtask, name="add_subtask"),
    path("remove_subtask/<int:subtask_id>", views.remove_subtask, name="remove_subtask"),
    path("edit_subtask/<int:subtask_id>", views.edit_subtask, name="edit_subtask"),
]