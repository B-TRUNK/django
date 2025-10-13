from django.urls import path
from . import views

urlpatterns = [

    path('' ,views.wlc ,name='wlc')

]