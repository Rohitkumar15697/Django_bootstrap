from django import forms

class myform(forms.Form):
    firstname=forms.CharField(max_length=122,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your first name'}))
    lastname=forms.CharField(max_length=122,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your last name'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))