from django.shortcuts import render,HttpResponse,redirect
from .forms import ShowDataForm
from .models import ShowData


# Create your views here.
def blog(request):
    fm=ShowDataForm()
    if request.method=='POST':
        fm=ShowDataForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('blog')
    else:
        data=ShowData.objects.all()[:2]
        return render(request, 'blog_app/blog.html',{'fm':fm,'data':data})