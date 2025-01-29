from django import forms
from .models import Student

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name", "roll_no", "city")
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Name'}),
            'roll_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Roll NO'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your City'}),
        }