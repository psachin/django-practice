# Create your views here.
# /home/sachin/plang/python/django/solutoire/auth/view.py
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login

def login_user(request):
    state= "Please login below .."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "logged in!"
            else:
                state = "BRUP!"
        else:
            state = "username/password incorrect"

    return render_to_response('auth.html', {'state':state,'username':username})
