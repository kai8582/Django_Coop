from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

app_name = "agenda"

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name="agenda/index.html"), name='index'),
    path('signup/',views.signup,name="signup"),
    path('login_result/', views.login, name='login'),

]