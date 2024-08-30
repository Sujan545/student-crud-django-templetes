from django import forms
from django.forms import ModelForm
from .models import Student

class StudentForm(ModelForm):
    class Meta:
        model=Student
        file = forms.FileField()
        #fields=['name','age','address','faculty']
        fields='__all__'