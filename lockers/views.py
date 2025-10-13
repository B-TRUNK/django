from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def wlc(request):
    return HttpResponse('Please Select a Locker')
