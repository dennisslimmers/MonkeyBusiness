from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#render function
@login_required(login_url="login/")
def renderadministrator(request):
    return render(request, "administrator.html")