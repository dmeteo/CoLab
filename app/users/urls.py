from django.urls import path

from app.users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('change-profile/<str:username>/', views.change_profile, name='change-profile'),
    path('<str:username>/', views.view_profile, name='profile'),
]