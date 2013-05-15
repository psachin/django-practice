# Create your views here.
from django.shortcuts import render_to_response

from users.models import FullName, Emp

def view_all_emp(request):
    emps = Emp.objects.all().order_by('id')
    return render_to_response('users/index.html',{'emps':emps})

def view_records(request):
    records = Record.objects.all().order_by('emp_id')
    return render_to_response('users/index.html',{'records':records})
    

