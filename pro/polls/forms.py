from django import forms

class RegistrationForm(forms.Form):

    def __init__(self, data):
        self.username = forms.CharField(max_length=30, initial="username")
        self.email = forms.EmailField(label="E-mail", initial="your e-mail ID")
        self.password1 = forms.CharField(label="Password",initial="your password")
        self.password2 = forms.CharField(label="Password Again",initial="re-type your password")
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).__init__()
        user.username = form.cleaned_data('username')
        user.email = form.cleaned_data('email')
        user.password1 = form.cleaned_data('password1')
        user.password2 = form.cleaned_data('password2')
        if commit:
            user.save()
        return user
    
