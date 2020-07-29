"""Defines URL patterns for tasks"""

from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all projects.
    path('taskmanager/', views.projects, name='projects'),
    # Detail page for a single project.
    path('taskmanager/<int:project_id>/', views.project, name='project'),
    # Detail page for a single project.
    path('taskmanager/task/<int:task_id>/', views.task, name='task'),
    # Page for adding a new project
    path('new_project/', views.new_project, name='new_project'),
    # Page for adding new task
    path('new_task/<int:project_id>/', views.new_task, name='new_task'),
    # Page for editing task
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
]