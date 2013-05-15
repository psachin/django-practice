# Create your views here.
from django import forms
from django.shortcuts import render_to_response, get_object_or_404
from datetime import datetime

class EmailForm(forms.Form): 
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'size':'50'})) 
    sender = forms.EmailField(max_length=30, widget=forms.TextInput(attrs={'size':'30'}))
    date = forms.DateField() 
    text = forms.CharField(max_length=200,widget=forms.Textarea(attrs={'rows':'6','cols':'75'}))


def contact_view(request):
    eForm = EmailForm()
    return render_to_response('contact_form.html',{'eForm':eForm})

    
