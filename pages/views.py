from django.shortcuts import render
from django.http import HttpResponse
from .models import Login
from .forms import *

# Create your views here.

person = {
    'file' : 'winrar',
    'size'  : 1321415135,
}

def index(request):
    return render(request ,'pages/index.html')

def about(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        form_data = Login(username=username, password=password)
        form_data.save()

    return render(request ,'pages/about.html' ,{'logform' : LoginForm ,'person' : person})

def contact_us(request):
    return HttpResponse('Call Us!')