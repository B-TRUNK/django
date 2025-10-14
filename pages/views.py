from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

person = {
    'file' : '',
    'size'  : 1321415135,
}

def index(request):
    return render(request ,'pages/index.html')

def about(request):
    return render(request ,'pages/about.html' ,person)

def contact_us(request):
    return HttpResponse('Call Us!')