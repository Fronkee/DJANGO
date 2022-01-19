from django.shortcuts import render
from django.http import HttpResponse
from .models import Category

# Create your views here.
def cats(request):
    data ={
        'title':'Categories',
        'cats' :Category.objects.all()
    }
    return render(request,'category/cats.html',data)

def subs(request):
    data = {
        'title' : 'Sub Categories'
    }
    return render(request,'category/subs.html')