# Create your views here.
from django.shortcuts import render_to_response

from testapp.models import Book
from testapp.models import Publisher
 
def view_latest_books(request):  
    books = Book.objects.all().order_by('-pubdate')
 
    return render_to_response('testapp/index.html', 
                             {'books': books})

def view_publishers(request):
    publishers = Publisher.objects.all().order_by('name')

    return render_to_response('testapp/pub_index.html',
                              {'pubs': publishers})
