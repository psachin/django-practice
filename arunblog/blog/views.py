from blog.models import Post
from django.shortcuts import render_to_response

def tagpage(request, tag):
    """
    view to display tags
    
    Arguments:
    - `request`:
    - `tag`:
    """
    posts = Post.objects.filter(tags__name=tag)
    context = {'posts':posts,
               'tag':tag,
               }
    return render_to_response("tagpage.html",context,)
    
    

    

    
