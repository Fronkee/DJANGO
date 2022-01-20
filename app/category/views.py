from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Category,SubCategory
from .forms import SubCatFrom,CatForm


# Create your views here.
def cats(request):
    data ={
        'title':'Categories',
        'cats' :Category.objects.all()
    }
    return render(request,'category/cats.html',data)

def createCat(request):
    if request.method == 'POST':
        form = CatForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/cats')
    else:
        return render(request,'category/create_cats.html',{'form':CatForm})

def subs(request):
    data = {
        'title' : 'Sub Categories'
    }
    subs =  SubCategory.objects.all()
    return render(request,'category/subs.html',{'subs':subs})

def createSub(request):
    if request.method == 'POST':
        form = SubCatFrom(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/cats/subs')
    else:
        return render(request,'category/create_subs.html',{'form':SubCatFrom})