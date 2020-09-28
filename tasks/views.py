from django.shortcuts import render, redirect
from .models import Project, TaskSection, Task
from .forms import ProjectForm, TaskForm, TaskSectionForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages
# Delete
from django.core.exceptions import PermissionDenied
from django.urls import reverse

def index(request):
    """The home page for tasks."""
    return render(request, 'tasks/index.html')

@login_required
def projects(request):
    """ Show all Projects"""
    projects = Project.objects.filter(owner=request.user).order_by('date_added')

    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'projects': projects, 'form': form}
    return render(request, 'tasks/projects.html', context)

@login_required
def project(request, project_id):
    """Show a single project and all it's tasks."""
    project = Project.objects.get(id=project_id)
    # Make sure the project belongs to the current user.
    if project.owner != request.user:
        raise Http404
    
    task_section = project.tasksection_set.order_by('-date_added')
    context = {'project':project, 'task_section': task_section}
    return render(request, 'tasks/project.html', context )

@login_required
def task_section(request, task_section_id):
    """Show a single task"""
    task_section = TaskSection.objects.get(id=task_section_id)
    tasks = task_section.task_set.all()



    # Make sure the task belongs to the current user.
    project = task_section.project
    if project.owner != request.user:
        raise Http404

    context = {'task_section': task_section, 'tasks': tasks, 'project': project}
    return render(request, 'tasks/task_section.html', context)


@login_required
def task(request, task_id):
    """Show a single task"""
    tasks = Task.objects.get(id=task_id)
    task_section = tasks.task_section

    # Make sure the task belongs to the current user.
    project = tasks.task_section.project
    if project.owner != request.user:
        raise Http404

    context = {'tasks':tasks, 'task_section': task_section, 'project': project}
    return render(request, 'tasks/task.html', context)

@login_required
def new_project(request):
    """Add new project"""

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ProjectForm()
    else:
        # POST data submitted; process data.
        form = ProjectForm(data=request.POST)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.owner = request.user
            new_project.save()
            return redirect('tasks:projects')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'tasks/new_project.html', context)


@login_required
def new_task_section(request, project_id):
    """ Add new task """
    project = Project.objects.get(id=project_id)

    # Make sure the task belongs to the current user.
    if project.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TaskSectionForm()
    else:
        # POST data submitted; process data.
        form = TaskSectionForm(data=request.POST)
        if form.is_valid():
            new_tasksection = form.save(commit=False)
            new_tasksection.project = project
            new_tasksection.save() 
            return redirect('tasks:project', project_id=project_id)

    # Display a blank or invalid form.
    context = {'project': project, 'form': form}
    return render(request, 'tasks/new_task_section.html', context)


@login_required
def new_task(request, task_section_id):
    """ Add new task """
    task_section = TaskSection.objects.get(id=task_section_id)
    
    
    # Make sure the task belongs to the current user.
    project = task_section.project
    if project.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TaskForm()
    else:
        # POST data submitted; process data.
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.task_section = task_section
            new_task.save() 
            return redirect('tasks:task_section', task_section_id=task_section_id)


    # Display a blank or invalid form.
    context = {'task_section': task_section, 'form': form}
    return render(request, 'tasks/new_task.html', context)


@login_required
def edit_project(request, project_id):
    """ Edit project """
    project = Project.objects.get(id=project_id)
    # project = task.project

    # Make sure the project belongs to the current user.
    if project.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # No data submitted; create form with pre-filled entry.
        form = ProjectForm(instance=project)
    else:
        # POST data submitted; process data.
        form = ProjectForm(instance=project, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:projects')
    
    context = {'project': project, 'form': form}
    return render(request, 'tasks/edit_project.html', context)


@login_required
def edit_task_section(request, task_section_id):
    """ Edit task """
    task_section = TaskSection.objects.get(id=task_section_id)
    project = task_section.project

    # Make sure the project belongs to the current user.
    if project.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # No data submitted; create form with pre-filled entry.
        form = TaskSectionForm(instance=task_section)
    else:
        # POST data submitted; process data.
        form = TaskSectionForm(instance=task_section, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:project', project_id=project.id)
    
    context = {'task_section': task_section, 'project': project, 'form': form}
    return render(request, 'tasks/edit_task_section.html', context)


@login_required
def edit_task(request, task_id):
    """ Edit task """
    task = Task.objects.get(id=task_id)
    project = task.task_section.project
    task_section = task.task_section

    # Make sure the project belongs to the current user.
    if project.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # No data submitted; create form with pre-filled entry.
        form = TaskForm(instance=task)
    else:
        # POST data submitted; process data.
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_section', task_section_id=task_section.id)
    
    context = {'task': task, 'project': project, 'form': form}
    return render(request, 'tasks/edit_task.html', context)



@login_required
def delete_project(request, project_id):
    """ Delete project in projects.html """
    project = Project.objects.get(id=project_id)

    # Make sure the project belongs to the current user.
    if project.owner != request.user:
        raise Http404

    if request.method == 'POST':
        project.delete()
        return redirect('tasks:projects')

    # context = {'project': project}
    # return render(request, 'tasks/delete_project.html', context)



@login_required
def delete_task_section(request, task_section_id):
    """ Delete project in project.html """
    task_section = TaskSection.objects.get(id=task_section_id)
    project = task_section.project

    # Make sure the project belongs to the current user.
    if project.owner != request.user:
        raise Http404

    if request.method == 'POST':
        task_section.delete()
        return redirect('tasks:project', project_id= project.id)



@login_required
def delete_task(request, task_id):
    """ Delete task """
    task = Task.objects.get(id=task_id)
    task_section = task.task_section
    project = task.task_section.project

    # Make sure the project belongs to the current user.
    if project.owner != request.user:
        raise Http404

    if request.method != 'POST':
        raise PermissionDenied
    else:
        task.delete()
        return redirect('tasks:task_section', task_section_id = task_section.id )

    
