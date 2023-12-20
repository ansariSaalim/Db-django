from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'date_of_birth', 'course']
    
    widgets = {
        'date_of_birth': forms.DateInput(attrs={'type': 'date', 'format': 'yyyy-mm-dd'}),
    }
