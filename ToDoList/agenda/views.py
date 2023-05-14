from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .forms import UserForm, ToDoForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import ToDos
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'agenda/index.html')



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
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            auth_login(request, user)
            return redirect('agenda:detail')
        else:
            return redirect('agenda:login')
           
        
    else:
        return render(request, 'agenda/login.html')
    
def logout(request):
    auth_logout(request)
    return redirect("agenda:index")



@login_required(login_url = 'agenda:login')
def details(request):
    user_datas = ToDos.objects.filter(author = request.user)

    return render (request, 'agenda/details.html', {'data':user_datas})



@login_required(login_url = "agenda:login")
def update(request,item_id):
    data = get_object_or_404(ToDos,pk = item_id)
    if request.method == "POST":
        form = ToDoForm(request.POST, instance = data)
        if form.is_valid():
            data = form.save(commit = False)
            data.pub_date = timezone.now()
            data.save()
            return redirect("agenda:detail")
        else:
            form = ToDoForm(instance=data)
            return render(request, 'agenda/createform.html',{'form':form})


    else:
        form = ToDoForm(instance=data)
        context = {'form':form}
        return render(request, 'agenda/createform.html',context)


@login_required(login_url = "agenda:login")
def delete(request, item_id):
    data = get_object_or_404(ToDos, pk = item_id)
    data.delete()
    return redirect("agenda:detail")



@login_required(login_url = 'agenda:login')
def create(request):
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            content = form.save(commit = False)
            content.pub_date = timezone.now()
            content.author = request.user
            content.save()
            return redirect('agenda:detail')
        else:
            return redirect('agenda:create')
    
    else:
        form = ToDoForm()
        return render(request, 'agenda/createform.html', {'form':form})
