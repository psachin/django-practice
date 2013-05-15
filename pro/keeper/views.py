# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from keeper.models import Author, Publisher, Book


def manage_author(request):
    auths = Author.objects.all()
    context = {"auths":auths,}
    return render_to_response("manage_authors.html",RequestContext(request,context))
