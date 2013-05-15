# Create your views here.
from django.shortcuts import HttpResponse, HttpResponseRedirect, render_to_response, get_object_or_404, render
from People.models import Person
from django.forms.models import modelform_factory, modelformset_factory
from django import forms

def index(request):
    plist = Person.objects.all()
    return render_to_response('person_index.html',{'plist':plist})

def details(request, pID="0", opts=()):
    p = get_object_or_404(Person, pk=pID)
    return render_to_response('person_details.html', {'p': p})

def person_form(request, pID='0'):
    PersonForm = modelform_factory(Person)
    f = PersonForm()
    message = 'Unkown Request'
    p = get_object_or_404(Person, pk=pID)
    
    if request.method == 'GET':
        PersonForm = modelform_factory(Person)
        f = PersonForm(instance=p)
        message = 'Editing person %s ' % p.name

    if request.method == 'POST':
        if request.POST['submit'] == 'update':
            message = 'Update Request for %s.' % p.name
            PersonForm = modelform_factory(Person)
            f = PersonForm(request.POST)
            if f.is_valid():
                message += ' Valid'
            else:
                message += ' Invalid'
    return render(request,'person_form.html',{'pForm':f,'message': message})

        

''''

def index(request):
    colors = ("BLUE","RED","GREEN")
    html="<HTML><BODY>\n"
    html += "<H1>Color Index</H1><HR>\n"
    for c in colors:
        html += "<FONT COLOR=%s><LI>%s</LI></FONT>\n" % (c,c)
    html += "</HTML></BODY>"
    return HttpResponse(html)


def details(request, pID="0"):
    response = HttpResponse()
    response.write("<html><body>\n")
    if pID == "0":
#        return HttpResponseRedirect('/people')
        response.write("<h1>Persons details index</h1><hr>")
        plist = Person.objects.all()
        for p in plist:
#            link = "<a href=\"Info/%d\">" % (p.userid)
            response.write("<li>%s</a></li>" % (p.name))
    else:
        response.write("<h1>Persons %s details index</h1><hr>" % pID)
        response.write("Detail goes here")
    response.write("</body></html>")
    return response
'''''
