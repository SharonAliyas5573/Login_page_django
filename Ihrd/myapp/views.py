from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required

@login_required
def welcome(request):
    username = request.user.username
    return render(request, 'myapp/welcome.html', {'username': username})


# Create your views here.
def homepage(request):
  return render(request = request, template_name="myapp/home.html" )




def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("myapp:welcome")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="myapp/register.html", context={"register_form":form})



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("myapp:welcome")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request=request, template_name="myapp/login.html", context={"login_form":form})
	
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("myapp:homepage")