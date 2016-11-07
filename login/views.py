from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from login.forms import LoginForm

# Create your views here.
# def index(request):
#     return render(request, "login.html")


def create(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect("/login/")
    else:
        return redirect("/")

def index(request):
    return render(request, "index.html")

@login_required(login_url="login/")
def home(request):
    return render(request, "home.html")
