from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ToDos

class UserForm(UserCreationForm):
    email=forms.EmailField(label="이메일")
    class Meta:
        model = User
        fields=('username','password1','password2','email')
        
class CreateForm():
    class Meta:
        model = ToDos
        fields=('content', 'pub_date', 'author')