from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from  .forms import RegistrationForm


# Create your views here.
def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")
    else:
        form = RegistrationForm()
    return render(request, "users/registration.html", {
        "form": form
    }) 


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): 
            login(request, form.get_user())
            return redirect("tasks:index")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {
        "form": form
    })


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("tasks:index")
    else:
        return render(request, "users/logout.html")