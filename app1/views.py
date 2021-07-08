from django.shortcuts import render, HttpResponse
from blog_app.models import ShowData


# Create your views here.
def index(request):
        data=ShowData.objects.all()[:1]
        return render(request, 'index.html',{'data':data})