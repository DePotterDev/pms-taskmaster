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
    # Detail page for task section.
    path('taskmanager/tasksection/<int:task_section_id>/', views.task_section, name='task_section'),
    # Detail page for a single task.
    path('taskmanager/task/<int:task_id>/', views.task, name='task'),

    # Page for adding a new project
    path('new_project/', views.new_project, name='new_project'),
    # Page for adding new task group
    path('new_task_section/<int:project_id>/', views.new_task_section, name='new_task_section'),
    # Page for adding new task
    path('new_tasks/<int:task_section_id>/', views.new_task, name='new_task'),

    # Page for editing task section
    path('edit_task_section/<int:task_section_id>/', views.edit_task_section, name='edit_task_section'),
    # Page for editing task
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    # Page for editing project
    path('edit_project/<str:project_id>/', views.edit_project, name='edit_project'),

    # Delete Project in projects.html
    path('delete/project/<int:project_id>/', views.delete_project, name='delete_project'),
    # Delete Task Section in project.html
    path('delete/task-section/<int:task_section_id>/', views.delete_task_section, name='delete_task_section'),
]

urlpatterns.extend(
    [
        #Delete Task in task.html
        path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    ]
)