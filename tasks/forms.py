from django import forms
from .models import Project, Task

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['text']
        labels = {'text': ''}

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text']
        labels = {'text': 'Task:'}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
