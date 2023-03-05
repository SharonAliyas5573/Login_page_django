from django.urls import path
from . import views

app_name = "myapp"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path('welcome', views.welcome, name='welcome'),
    path("logout", views.logout_request, name= "logout"),
    
]