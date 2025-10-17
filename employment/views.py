from django.shortcuts import render

# Create your views here.

def emp_view(request):
    return render(request, 'emp/index.html')