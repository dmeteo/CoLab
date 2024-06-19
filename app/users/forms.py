from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from app.users.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username', 'password')

    username = forms.CharField()
    password = forms.CharField()


class UserSignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "surname",
            "email",
            "phone_number",
            "password1",
            "password2",
        )
    
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    surname = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    

class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "username",
            "first_name",
            "last_name",
            "surname",
            "email",
            "phone_number",)

    image = forms.ImageField(required=False)
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    surname = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()