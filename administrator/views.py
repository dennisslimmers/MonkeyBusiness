from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#render function
@login_required(login_url="login/")
def renderAdministrator(request):
    users = User.objects.all()
    return render(request, "administrator.html", {"users": users})

@login_required(login_url="login/")
def renderEditUsers(request):
    users = User.objects.all()
    return render(request, "editusers.html", {"users": users})

def makeUserStaff(request):
    # for item in request.POST:
    #     if item != request.POST["c

    post = request.POST.copy()
    del post["csrfmiddlewaretoken"]

    return render(request, "test.html", {"post":post})

