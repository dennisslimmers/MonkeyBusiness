from django.shortcuts import render, redirect
from login.forms import loginForm

# Create your views here.
def index(request):
    return render(request, "login.html")


def create(request):
    if request.method == "POST":
        print(request.POST)
        print("test ")
        firstname = request.POSTs
        return render(request, "index.html", {"firstname": firstname})
    else:
        return redirect("/")