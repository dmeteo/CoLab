from django import forms

from projects.models import Project



class ProjectForm():

    class Meta():
        model = Project
        fields = ('name', 'about', 'rating')

    name = forms.CharField()
    about = forms.CharField()
    rating = forms.FloatField()