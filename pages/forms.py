from django import forms

#label
#initial
#disabled
#help_text
#widget
#required


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='name', initial='user_name', required=True)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True)
