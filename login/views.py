from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from login.forms import LoginForm
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
# def index(request):
#     return render(request, "login.html")


def create(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect("/login/")
    else:
        return redirect("/")

def changePassword(request):
    if request.method == "POST":
        passwordI = request.POST["passwordI"]
        passwordII = request.POST["passwordII"]
        if passwordI == passwordII:
            username = request.user
            print(username)
            u = User.objects.get(username=username)
            u.set_password(passwordI)
            u.save()
            return redirect("home")
        else:
            return redirect("home")
    else:
        return redirect("home")

def index(request):
    return render(request, "index.html")

@login_required(login_url="login/")
def home(request):
    return render(request, "home.html")

def pdfBuilder(request):
    username = request.user
    date = datetime.now().strftime('%Y-%m-%d')
    amount = ""
    product = ""

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Vacancy-' + str(product) + '.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(50, 800, "Hi " + str(username) + ",")
    p.drawString(50, 780, "This is a courtesy email to let you know that your payments of €" + str(amount))
    p.drawString(50, 770, "for " + str(product) + " are now overdue. We didn't receive any payment")
    p.drawString(50, 760, "which means that the total outstanding is now €" + str(amount) + ".")

    p.drawString(50, 730, "We would greatly appreciate you fixing up this outstanding amount at your soonest possible")
    p.drawString(50, 720, "convenience. You can do this by calling 071-3617182 and paying by credit card.")

    p.drawString(50, 700, "You can also pay the outstanding amount by direct deposit into our account.")
    p.drawString(50, 690, "The account name is " + str(username) + ",")
    p.drawString(50, 680, "the BSB is 033003 and the account number is 234.")
    p.drawString(50, 670, "Please make sure you put your name or quote this number 033003")
    p.drawString(50, 660, "when paying by direct deposit into our bank account.")

    p.drawString(50, 640, "We look forward to receiving the outstanding funds shortly.")

    p.drawString(50, 620, "Yours Sincerely,")
    p.drawString(50, 590, "MonkeyBusiness")
    p.drawString(50, 560, str(date))

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response