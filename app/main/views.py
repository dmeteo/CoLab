from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': "home",
        'content': "Главная страница",
        'list': ['first', 'sec'],
        'dict': {'first': 1},
        'is_authentificated': False,
    }

    return render(request, "main/index.html", context)

def about(request):
    return HttpResponse("About page")