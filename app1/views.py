from django.shortcuts import render
from .forms import ShowDataForm
from .models import ShowData


# Create your views here.
def index(request):
    fm=ShowDataForm()
    return render(request, 'index.html',{'fm':fm})