# Create your views here.
from django.shortcuts import render

def my_report(request):

    template = "myapp/my_report.html"
    # Initialise the report
    val_list = [['foo', 32], ['bar', 64], ['baz', 96]]
    context = {
        'values': val_list,
    }

    return render(request, template, context)
