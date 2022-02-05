from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm #can be used default form
from .forms import *
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        print("POST ")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Register Success Mr. {username}')
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request,'user/register.html',{'form':form})

#12345han