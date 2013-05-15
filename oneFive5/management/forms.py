from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    """ Require email address when a user signs up """
    email = forms.EmailField(label='Email address', max_length=75)
    
    class Meta:
        model = User
        fields = ('username', 'email',) 

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            user = User.objects.get(email=email)
            raise forms.ValidationError("This email address already exists. Did you forget your password?")
        except User.DoesNotExist:
            return email
        
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        user.is_active = True # change to false if using email activation
        if commit:
            user.save()
            
        return user

class Register(UserCreationForm):
    """my form"""
    sr_no = forms.IntegerField(max_value=10,required=True)

    class Meta:
        model = User
        fields = ('username','password1','password2','sr_no')
        
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data["username"]
        # user.firs_tname = self.cleaned_data["first_name"]
        # user.last_name = self.cleaned_data["last_name"]
        # user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"])
        user.sr_no = self.cleaned_data["sr_no"]
        user.is_active = True
        if commit:
            user.save()
        return user
