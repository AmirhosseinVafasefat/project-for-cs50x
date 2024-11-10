from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=64)
    user = models.ForeignKey(User, blank=False, related_name="tasks", on_delete= models.CASCADE)

    def __str__(self) -> str:
        return f"{self.task} {self.id}"
    

class Subtask(models.Model):
    subtask = models.CharField(max_length=64)
    task = models.ForeignKey(Task, blank=False, related_name="subtasks", on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.subtask}"

