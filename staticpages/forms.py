from django import forms

class NameForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(label='Your name', max_length=100, widget=forms.PasswordInput)