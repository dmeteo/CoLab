from django.urls import path

from app.users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('<str:username>/', views.profile, name='profile'),
]