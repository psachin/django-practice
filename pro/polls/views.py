# Create your views here.
from django.shortcuts import render_to_response, RequestContext, render, HttpResponse
from django.contrib.auth import authenticate, login
from polls.forms import RegistrationForm

def contact(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<html>info submitted</html>')
    else:
        form = RegistrationForm()
    return render(request,'contact.html',{'form':form})















