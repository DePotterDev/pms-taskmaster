from django import forms
from .models import Project, TaskSection, Task

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text' : forms.TextInput(attrs={'class': 'form-control my3 col-md-4'})
        }

class TaskSectionForm(forms.ModelForm):
    class Meta:
        model = TaskSection
        fields = ['title', 'desc']
        labels = {'title': 'Title:', 'desc': 'Description'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-3'}),
            'desc': forms.Textarea(attrs={'cols':20, 'class': 'form-control my-3'}),     
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'text', 'priority']
        labels = {'title': 'Title:', 'priority': 'priority'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-3'}),
            'text': forms.Textarea(attrs={'cols': 30, 'class': 'form-control my-3'}),
        }
