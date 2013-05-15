from django import forms
from engine.models import Profile

class UserRegisterForm(forms.Form):
    user = forms.CharField(max_length=10)
    
    
