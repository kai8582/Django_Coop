from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserForm
from django.contrib.auth import authenticate, login

# Create your views here.
def signup(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:index')

        else:
            return render(request,'agenda/signup.html',{'form':form})
    else:
        form = UserForm()
        return render(request,'agenda/signup.html',{'form':form})


def login(request):
    return HttpResponse("Login Successful!!")