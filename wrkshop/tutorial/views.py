# Create your viecutews here.
from django.shortcuts import render_to_response
from django.forms.models import modelformset_factory
from tutorial.models import Book

 
def view_latest_books(request):  
    books = Book.objects.all().order_by('-pubdate')
 
    return render_to_response('tutorial/index.html', 
                             {'books': books})

def view_books(request):
    bookformset = modelformset_factory(Book)
    if request.POST:
        formset = bookformset(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
    else:
        formset = bookformset()
    return render_to_response('manage_authors.html', 
                             {'formset': formset})
    














