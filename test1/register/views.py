from django.shortcuts import HttpResponseRedirect, render_to_response, HttpResponse
from django.template import RequestContext
from forms import Register



def register(request):
    """
    generate user register form
    """
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                success = "<html>sign_up_success</html>"
                return HttpResponse(success)
    else:
        form = Register()
        context = {'form':form}
        return render_to_response("register.html",
                                  context,
                                  context_instance=RequestContext(request))
    
                
            
    



