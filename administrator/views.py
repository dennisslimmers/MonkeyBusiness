from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#render function
@login_required(login_url="login/")
def renderadministrator(request):
    users = User.objects.all()
    return render(request, "administrator.html", {"users": users})

