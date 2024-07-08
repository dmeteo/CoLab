from django.shortcuts import render

from app.users.models import User
from app.projects.models import Project


def index(request):

    context = {
        'title': 'Главная',
    }

    return render(request, 'main/index.html', context)

def feed(request):
    users_list = User.objects.all()

    context = {
            "title": "Лента",
            "users_list": users_list,
        }
    return render(request, 'main/feed.html', context)

def feed_projects(request):
    projects_list = Project.objects.all()

    context = {
            "title": "Лента проектов",
            "projects_list": projects_list,
        }
    return render(request, 'main/feed-projects.html', context)