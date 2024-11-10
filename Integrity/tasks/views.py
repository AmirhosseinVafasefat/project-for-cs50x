from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden
from  django.urls import reverse
from .forms import NewTaskForm, SubtaskForm
from .models import Task, Subtask



# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    user = request.user

    if request.method == "GET":
        taskform = NewTaskForm()
        subtaskform = SubtaskForm()

    if request.method == "POST":
        taskform = NewTaskForm(request.POST)
        subtaskform = SubtaskForm(request.POST)

        if taskform.is_valid() and subtaskform.is_valid():

            # save task
            task = Task(task=taskform.cleaned_data["task"], user=user)
            task.save()

            # save subtasks
            subtask = subtaskform.cleaned_data["subtask"]
            if subtask:
                subtask = Subtask(task=task, subtask= subtaskform.cleaned_data["subtask"])
                subtask.save()

            taskform = NewTaskForm()
            subtaskform = SubtaskForm()
            
        else:
            tasks = user.tasks.all()
            return render(request, "tasks/index.html", {
                "taskform": taskform,
                "subtaskform": subtaskform,
                "tasks": tasks
            })
        
    tasks = user.tasks.all()
    
    return render(request, "tasks/index.html", {
        "taskform": taskform,
        "subtaskform": subtaskform,
        "tasks": tasks,
    })

def remove_task(request, task_id):
    if request.method == "POST":
        user = request.user
        task = Task.objects.get(pk=task_id)
        if user == task.user:
            task.delete()
    return HttpResponseRedirect(reverse("tasks:index"))

def edit_task(request, task_id):
    user = request.user
    try:
        task = Task.objects.get(pk=task_id)
        if user == task.user:
            taskform = NewTaskForm({'task': f"{task.task}"})
            if request.method == "POST":
                taskform = NewTaskForm(request.POST)
                if taskform.is_valid():
                    task.task = taskform.cleaned_data["task"]
                    task.save()
                    return HttpResponseRedirect(reverse("tasks:index"))
            
            return render(request, "tasks/edit.html", {
                "task": task,
                "form": taskform
            })
    except Task.DoesNotExist:
        return HttpResponseForbidden("Not allowed to edit task")

    else:
        return HttpResponseForbidden("Not allowed to edit task")

def add_subtask(request, task_id):
    user = request.user
    task = Task.objects.get(pk=task_id)

    if not user == task.user:
        return HttpResponseForbidden("Not allowed to edit task")
    
    subtaskform = SubtaskForm()
    if request.method == "POST":
        subtaskform = SubtaskForm(request.POST)
        if subtaskform.is_valid():
            newSubtask = subtaskform.cleaned_data["subtask"]
            subtask = Subtask(subtask=newSubtask, task=task)
            subtask.save()
            return HttpResponseRedirect(reverse("tasks:index")) 

    return render(request, "tasks/add_subtask.html", {
        "task": task,
        "form": subtaskform
    })

def remove_subtask(request, subtask_id):
    if request.method == "POST":
        user = request.user
        subtask = Subtask.objects.get(pk=subtask_id)
        if user == subtask.task.user:
            subtask.delete()
    return HttpResponseRedirect(reverse("tasks:index"))

def edit_subtask(request, subtask_id):
    user = request.user
    try:
        subtask = Subtask.objects.get(pk=subtask_id)
        if user == subtask.task.user:
            subtaskform = SubtaskForm({'subtask': f"{subtask.subtask}"})
            if request.method == "POST":
                subtaskform = SubtaskForm(request.POST)
                if subtaskform.is_valid():
                    subtask.subtask = subtaskform.cleaned_data["subtask"]
                    subtask.save()
                    return HttpResponseRedirect(reverse("tasks:index"))
            
            return render(request, "tasks/edit.html", {
                "subtask": subtask,
                "form": subtaskform
            })
    except Task.DoesNotExist:
        return HttpResponseForbidden("Not allowed to edit subtask")

    else:
        return HttpResponseForbidden("Not allowed to edit subtask")