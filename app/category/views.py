from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Category,SubCategory
from .forms import SubCatFrom,CatForm
from django.contrib.auth.decorators import login_required
from .decorators import allow_users


# Create your views here.
def home(request):
    return render(request,'category/home.html')


def cats(request):
    data ={
        'title':'Categories',
        'cats' :Category.objects.all()
    }
    return render(request,'category/cats.html',data)

@allow_users(allowed_roles=['admins'])
@login_required
def createCat(request):
    if request.method == 'POST':
        form = CatForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/cats')
    else:
        print("get method")
        form = CatForm()

    return render(request,'category/create_cats.html',{'form':form})

def catDelete(request,id):
    result = Category.objects.get(pk=id)
    result.delete()
    return redirect('/cats')
    
def catEdit(request,id):
    result = Category.objects.get(pk=id)
    if request.method == 'POST':
        form = CatForm(request.POST,request.FILES,instance=result)
        if form.is_valid():
            form.save()
            return redirect('/cats')
    else:
        form = CatForm(instance=result)
    
    return render(request,'category/cat_edit.html',{'form':form})


# for SubCategory
def subs(request):
    print("Sub page")
    data = {
        'title' : 'Sub Categories'
    }
    subs =  SubCategory.objects.all()
    return render(request,'category/subs.html',{'subs':subs})


@login_required
def createSub(request):
    if request.method == 'POST':
        form = SubCatFrom(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/cats/subs')
    else:
        print('Get method')
        form = SubCatFrom()
    return render(request,'category/create_subs.html',{'form':form})

def subDelete(request,id):
    result = SubCategory.objects.get(pk=id)
    result.delete()
    return redirect('/cats/subs')


def subEdit(request,id):
    result = SubCategory.objects.get(pk=id)
    if request.method == 'POST':
        form = SubCatFrom(request.POST,request.FILES,instance=result)
        if form.is_valid():
            form.save()
            return redirect('/cats/subs')
    else:
        form = SubCatFrom(instance=result)
    return render(request,'category/sub_edit.html',{'form':form})