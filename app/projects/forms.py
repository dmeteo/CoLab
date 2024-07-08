from django import forms

from app.projects.models import Project

class ProjectForm(forms.ModelForm):

    class Meta():
        model = Project
        fields = ('name', 
                  'about', 
                  'rating',)

    name = forms.CharField()
    about = forms.CharField()
    rating = forms.FloatField()