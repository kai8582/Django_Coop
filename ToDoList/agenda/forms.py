from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# 회원가입시 auth_user에 비밀번호는 암호화시켜서 저장, username은 그대로해서 저장한다.
class UserForm(UserCreationForm):
    email=forms.EmailField(label="이메일")
    class Meta:
        model = User
        fields=('username','password1','password2','email')