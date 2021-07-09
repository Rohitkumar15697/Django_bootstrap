from django import forms
from .models import ShowData

class ShowDataForm(forms.ModelForm):
    class Meta:
        model=ShowData
        fields="__all__"
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),'post': forms.Textarea(attrs={'class':'form-control','style':'height:200px;'})}