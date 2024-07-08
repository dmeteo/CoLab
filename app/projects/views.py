from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from app.projects.forms import ProjectForm
from app.projects.models import Project

def project_card(request, name):
    project = get_object_or_404(Project, name=name)

    context = {
        'title': "Карточка проекта "+project.name,
        'project': project,
        'name': name,
    }
    return render(request, 'projects/project.html', context)

def edit_project_card(request, name):
    project = Project.objects.get(name=name)
    if request.method == 'POST':
        projectForm = ProjectForm(data=request.POST, instance=project)
        if projectForm.is_valid():
            project.save()
            messages.success(request, "Карточка проекта успешно обновлена")
            return HttpResponseRedirect(reverse(f'{request.project.name}'))
    else:
        project = ProjectForm(instance=project)  

    context = {
        'title': 'Редактирование профиля',
        'project': project,
        'name': name
    }
    return render(request, 'projects/edit-project.html', context)   



def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST or None)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('main:index')
    else:
        form = ProjectForm()
    
    context = {
        'form': form,
    }
    return render(request, 'projects/create-project.html', context) 