from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import connection


@login_required(login_url="login/")
def renderAdministrator(request):
    users = User.objects.all()
    return render(request, "administrator.html", {"users": users})


@login_required(login_url="login/")
def renderEditUsers(request):
    users = User.objects.all()
    return render(request, "editusers.html", {"users": users})

def renderAddCourse(request):
    return render(request, "addcourse.html")


def makeUserStaff(request):
    post = request.POST.copy()
    del post["csrfmiddlewaretoken"]

    array_keys = list(post.keys())

    for key in array_keys:
        with connection.cursor() as cursor:
            cursor.execute("SELECT is_staff FROM auth_user WHERE username = '" + key + "'")
            is_staff = cursor.fetchone()

            if not is_staff[0]:
                cursor.execute("UPDATE auth_user SET is_staff = 1 WHERE username = '"+ key +"'")

    return render(request, "editusers.html")

