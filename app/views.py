from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *

def student(request):
    form=StudentForm()
    if request.method=='POST':
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            return HttpResponse('Form is Validated Succeefully')

    return render(request,'student.html',context={'form':form})

def data(request,name):
    return HttpResponse('person name is {}'.format(name))