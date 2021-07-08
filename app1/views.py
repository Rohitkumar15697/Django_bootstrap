from app1.forms import ShowDataForm
from django.shortcuts import render
#from .models import ShowData
#from .forms import ShowDataForm


# Create your views here.


def index(request):
    
    return render(request, 'index.html')