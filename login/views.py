from django.shortcuts import render
from login.forms import loginForm

# Create your views here.
def index(request):
    return render(request, "login.html")

# login method
def login(request):
    if request.method == "post":
        form = loginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]

            return render(request, "index.html", {"username": username})