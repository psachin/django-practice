# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('clock.html',{'now':now})

''''
    now = datetime.datetime.now()
    html = "<html><body>It is now : %s</body></html>" %(now)
    return HttpResponse(html)
'''''
def hours_ahead(request, arg):
    html = "<html><body>the second argument is : %s</body></html>" %(arg)
    return HttpResponse(html)

def sample_template(request):
    username="sachin"
    return render_to_response('mysite.html',locals()) # locals() will
                                                      # include all
                                                      # the variables
                                                      # values at the
                                                      # time of
                                                      # function
                                                      # execution

      # return render_to_response('mysite.html',{'username':username})

def day_archive(request,  year, mount, day):
    # date time
    date = datetime.date(int(year), int(month), int(day))


def load_image(request):
    image_data = open("/home/sachin/plang/python/django/mysite/books/headshot/icfoss.png","rb").read()
    return HttpResponse(image_data, mimetype="image/png")




