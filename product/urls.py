from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.products ,name='products'),
    path('p', views.product ,name='product'),

]