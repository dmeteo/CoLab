from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from app.users.models import User, Profile


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

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        if not (phone_number.startswith('+79') or phone_number.startswith('89')):
            raise forms.ValidationError('Неверный номер телефона')
        return phone_number
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not (first_name.isalpha()):
            raise forms.ValidationError('Неверное имя')
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not (last_name.isalpha()):
            raise forms.ValidationError('Неверная фамилия')
        return last_name
    
    def clean_surname(self):
        surname = self.cleaned_data['surname']
        if not (surname.isalpha()):
            raise forms.ValidationError('Неверное отчество')
        return surname
    
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    surname = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('institute',
                  'trend',
                  'course',
                  'bio')
        
    institute = forms.CharField()
    trend = forms.CharField()
    course = forms.CharField()
    bio = forms.CharField()


class UserForm(UserChangeForm):
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
        
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        if not (phone_number.startswith('+79') or phone_number.startswith('89')):
            raise forms.ValidationError('Неверный номер телефона')
        return phone_number
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not (first_name.isalpha()):
            raise forms.ValidationError('Неверное имя')
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not (last_name.isalpha()):
            raise forms.ValidationError('Неверная фамилия')
        return last_name
    
    def clean_surname(self):
        surname = self.cleaned_data['surname']
        if not (surname.isalpha()):
            raise forms.ValidationError('Неверное отчество')
        return surname
        

    image = forms.ImageField(required=False)
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    surname = forms.CharField()
    email = forms.CharField()
    phone_number = forms.CharField()

    def get_username(self):
        return self.username