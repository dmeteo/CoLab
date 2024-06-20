from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, UpdateView

from app.users.models import User, Profile
from app.users.forms import UserLoginForm, UserSignUpForm, UserForm, ProfileUpdateForm

def login(request):
    if request.user.is_authenticated: 
        redirect(reverse('main:index'))
    elif request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в аккаунт")
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)

def signup(request):
    if request.user.is_authenticated: 
        redirect(reverse('main:index'))
    elif request.method == 'POST':
        form = UserSignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)

            messages.success(request, f"{user.username}, Вы успешно зарегистрированы и вошли в аккаунт")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserSignUpForm()

    context = {
        'title': 'Home - Регистрация',
        'form': form
    }
    return render(request, 'users/signup.html', context)
    

@login_required
def change_profile(request, username):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST, instance=request.user, files=request.FILES)
        profile_form = ProfileUpdateForm(data=request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Профайл успешно обновлен")
            return HttpResponseRedirect(reverse(f'{request.user.username}'))
    else:
        user_form = UserForm(instance=request.user)  
        profile_form = ProfileUpdateForm(instance=request.user)

    context = {
        'title': 'Home - Кабинет',
        'user_form': user_form,
        'profile_form': profile_form,
        'username': username
    }
    return render(request, 'users/change-profile.html', context)   

def view_profile(request, username):
    user = User.objects.get(username=username)
    # profile = Profile.objects.get(pk=user.pk)

    context = {
        'title': 'Home - Кабинет',
        'first_name': user.first_name,
        'last_name': user.last_name,
        'surname': user.surname,
        'university': 'УрФУ',
        # 'institute': profile.institute,
        # 'trend': profile.trend,
        # 'course': profile.course,
        # 'bio': profile.bio,
        'username': username
    }
    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))