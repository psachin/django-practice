# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from forms import ContactForm
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.cleaned_data.get('sender','noreply@example.com')
            send_mail("Feedback from your site, topic: %s,message,sender,['administrator@example.com']")
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
        return render_to_response('contact.html',locals())

    
