from django.urls import path

from app.main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('feed/', views.feed, name='feed'),
    path('feed-projects', views.feed_projects, name='feed-projects')
]