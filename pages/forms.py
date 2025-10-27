from django import forms
from .models import *

#label
#initial
#disabled
#help_text
#widget
#required



#class LoginForm(forms.Form):   
    #username = forms.CharField(max_length=50, label='name', initial='user_name', required=True)
    #password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True)

#grasp fields from the model
class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        #get all fields
        fields = '__all__'
        #get a specific field
        #fields = ['password', 'password']

    