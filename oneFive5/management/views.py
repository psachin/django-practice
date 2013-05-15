# Create your views here.
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate, login


from forms import SignUpForm, Register
from random import choice
from string import letters

def sign_up(request):
    """ User sign up form """
    if request.method == 'POST':
        data = request.POST.copy() # so we can manipulate data
        # random username
        data['username'] =  ''.join([choice(letters) for i in xrange(30)])
        form = SignUpForm(data)
            
        if form.is_valid():
            user = form.save()
            success="<html>sign_up_success</html>"
            return HttpResponse(success)
    else:
        form = SignUpForm()

    return render_to_response('sign_up.html', {'form':form}, context_instance=RequestContext(request))


def register(request):
    """my register"""
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            user = form.save()
            success="<html><h1 align=center>Sign_up_success</h1></html>"
            return HttpResponse(success)
    else:
        form = Register()
        
    return render_to_response('sign_up.html', {'form':form}, context_instance=RequestContext(request))

def index(request):
     return HttpResponseRedirect('/register')

''''
def register(request):
    if request.method =='POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            #user = User.objects.create_user(form.cleaned_data['username'], None, form.cleaned_data['password1'])
            user_form.save()
            user = authenticate(username=username,password=password)
            login(request, user)
            html="<html>Welcome</html>"
            return HttpResponse(html) # Redirect after POST
    else:
        form = UserCreationForm() # An unbound form
    return render_to_response("register.html", {'form': form,},context_instance=RequestContext(request))
'''













