from django import forms
from .models import ShowData

class ShowDataForm(forms.ModelForm):
    class Meta:
        model=ShowData
        fields="__all__"
        widgets = {'post': forms.Textarea(attrs={'style': 'height: 200px;width:400px'})}