# Create your views here.

from blog.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    """render index.html
    
    Arguments:
    - `request`:
    """
    context = {'categories': Category.objects.all(),
               'posts':Blog.objects.all()[:5]}
    return render_to_response('index.html',
                              context,)


def view_post(request, slug):
    """render posts
    
    Arguments:
    - `request`:
    - `slug`:
    """
    context = {'post':get_object_or_404(Blog, slug=slug)}
    render_to_response('view_post.html',
                       context)

def view_category(request, slug):
    """view categories
    
    Arguments:
    - `request`:
    - `slug`:
    """
    category = get_object_or_404(Category, slug=slug)
    context = {'category':category,
               'posts':Blog.objects.filter(category=category)[:5]}
    
    render_to_response('view_category.html', 
                       context)

    



    
