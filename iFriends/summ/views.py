# Create your views here.
from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect
from summ.models import CalcForm
from django.template import RequestContext
from forms import Output

def calculate(request):
    c = CalcForm()
    if request.method == 'POST':
        form_out = CalcForm(request.POST)
        if form_out.is_valid():
            clean_data = form_out.cleaned_data
            form_out.save()
            field1 = clean_data['field1']
            field2 = clean_data['field2']
            answer = field1 + field2
            return render_to_response('sum.html',{'calculator':c,'answer':answer},context_instance=RequestContext(request))
    else:
        return render_to_response('sum.html',{'calculator':c},context_instance=RequestContext(request))

def add(request):
    form = Output()
    if request.method == 'POST':
        form = Output(request.POST)
        if form.is_valid():
            clean_form  = form.cleaned_data
            input1 = clean_form['input1']
            input2 = clean_form['input2']
            out = input1 + input2
            return render_to_response('add.html',{'calculator':form,'answer':out},context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect("/admin")
    else:
        return render_to_response('add.html',{'calculator':form},context_instance=RequestContext(request))


def value(request):
    return render_to_response('value.html')

def jq(request):
    return render_to_response('jq.html')
