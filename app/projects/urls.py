from django.urls import path

from app.projects import views

app_name = 'projects'

urlpatterns = [
    path('create-project/', views.create_project, name='create-project'),
    path('edit-project/<str:name>/', views.edit_project_card, name='edit-project'),
    path('<str:name>/', views.project_card, name='project'),
]