from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from settings import MEDIA_URL, MEDIA_ROOT

from forum.models import Forum

def main(request):
    """main listing
    
    Arguments:
    - `request`:
    """
    forums = Forum.objects.all()
    return render_to_response("forum/list.html", 
                              dict(forums=forums, 
                                   user=request.user))





