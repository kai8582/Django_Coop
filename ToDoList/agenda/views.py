from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import ToDos

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


def update(request):
    #학선님 업데이트 뷰 입니다! 제 생각에는 업데이트 버튼 클릭 시 pk 를 이용한 데이터조회후에 create form 으로 간 다음 request.method == "POST" 로 데이터 수정 가능할것같습니다!
    return

def delete(request):
    #선우님 삭제 뷰 입니다! 업데이트와 비슷하게 클릭 시 pk를 이용한 데이터 조회후에 삭제. 따로 render html파일은 안만들어도 될거 같습니다! redirect로!
    return

def create(request):
    #은혜님 뷰! 제 생각에 createform.html 파일을 만들어야할거같습니다. 또 forms.py파일에 새로운 클래스와 데이터베이스 연동이 필요할듯합니다! 
    return
