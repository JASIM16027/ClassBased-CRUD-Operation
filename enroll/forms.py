from django.core import validators
from django import forms
from .models import User

from .models import User
class StudentAddForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','password','email']
        labels = {'name':'Enter Name','password':'Enter Password','email':'Enter Email'}
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
        'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'})
        }