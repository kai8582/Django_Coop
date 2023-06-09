from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import UserForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

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



@login_required(login_url = 'agenda:index')
def details(request):
    # 여기가 아마 진용님이 작업하실 뷰 인것같습니다. 여기서 초기화면 구현 로직 짜시면 됩니다! 저엿다면 objects.get(유저정보)로 데이터목록들을 불러올거같습니다!
    # url pattern과 function 이름도 제가 마음대로 햇으니 마음대로 수정하셔도 됩니다! 진용님파트가 제일 중요할거같네요ㅎㅎ HTML도 새로 만들어야될거같습니다. 추가로 settings.py파일에 login_redirect_url도 수정이 필요할거같습니다
    user = request.user
    return render (request, 'agenda/details.html', {'user': user})


#학선님 업데이트 뷰 입니다!
#제 생각에는 업데이트 버튼 클릭 시 pk 를 이용한 데이터조회후에 create form 으로 간 다음 request.method == "POST" 로 데이터 수정 가능할것같습니다!
@login_required(login_url='agenda:index')
def update(request,id):
    data=get_object_or_404(ToDos,pk=id)
    if request.method=="POST":
        form=ToDoForm(request.POST, instance=data)
        if form.is_valid():
            data=form.save(commit=False)
            data.pub_date=timezone.now()
            data.save()
        else:
            form=ToDoForm(instance=data)
            return render(request, '생성페이지',{'form':form})
    else:
        form=ToDoForm(instance=data)
        context={'form':form}
        return render(request,'생성페이지',context)



def delete(request):
    #선우님 삭제 뷰 입니다! 업데이트와 비슷하게 클릭 시 pk를 이용한 데이터 조회후에 삭제. 따로 render html파일은 안만들어도 될거 같습니다! redirect로!
    return

def create(request):
    #은혜님 뷰! 제 생각에 createform.html 파일을 만들어야할거같습니다. 또 forms.py파일에 새로운 클래스와 데이터베이스 연동이 필요할듯합니다! 
    return
