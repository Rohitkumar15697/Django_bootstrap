from django.shortcuts import render
from .forms import ShowDataForm
from .models import ShowData


# Create your views here.
def index(request):
    fm=ShowDataForm()
    data=ShowData.objects.all()
    return render(request, 'index.html',{'fm':fm,'data':data})