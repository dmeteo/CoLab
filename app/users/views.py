from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from app.users.models import User
from app.users.forms import UserLoginForm, UserSignUpForm, ProfileForm


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
def profile(request, username):
    user_profile = get_object_or_404(User, username=username)
    if user_profile.username == request.user.username:
        if request.method == 'POST':
            form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Профайл успешно обновлен")
                return HttpResponseRedirect(reverse(f'{request.user.username}'))
        else:
            form = ProfileForm(instance=request.user)    

        context = {
            'title': 'Home - Кабинет',
            'form': form,
            'username': username
        }
        return render(request, 'users/profile_for_owner.html', context)
    else:
        return render(request, 'users/other_profile.html', {'user_profile': user_profile})

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))