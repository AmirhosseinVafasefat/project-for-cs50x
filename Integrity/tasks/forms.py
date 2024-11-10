from django import forms
from django.forms import ModelForm
from .models import Task, Subtask


class NewTaskForm(ModelForm):
    class Meta:
        model=Task
        fields=['task']


class SubtaskForm(forms.Form):
    subtask = forms.CharField(max_length=64, required=False)