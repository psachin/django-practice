# Create your views here.
from django.shortcuts import render_to_response, render, HttpResponse
from django.forms.models import modelformset_factory
from books.models import Author, Book
from django.template import RequestContext


def add_publisher(request):
    if request.POST:
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('thanks.html')
    else:
        form = PublisherForm()
    return render_to_response('add.html')

def manage_authors(request):
    AuthorFormSet = modelformset_factory(Author)
    if request.method == 'POST':
        formset = AuthorFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return render_to_response('thanks.html')
    else:
        formset = AuthorFormSet()
    return render(request,"manage_authors.html",{'formset':formset,})

def show_authors(request):
    authors = Author.objects.all()
    return render_to_response('show_authors.html',{'authors':authors})


'''
def manage_author(request):
auths = Author.objects.all()
context = {"auths":auths,}
return render_to_response("manage_authors.html",RequestContext(request,context))

'''
