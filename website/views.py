from django.conf import settings
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
import hashlib
import random
# login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from adpanel.models import Template as TemplateModel 
from adpanel.models import Video as VideoModel
from adpanel.models import Motion as Motion

def Home(request):
    return render(request, 'web/base.html')

def Template(request):
    templates = TemplateModel.objects.all().order_by('-id')
    return render(request,'web/template.html',{'templates' : templates})


def Motion_graphics(request):
    motions = Motion.objects.all().order_by('-id')
    return render(request ,'web/motion_graphics.html',{'motions': motions})

def Video(request):
    videos = VideoModel.objects.all().order_by('-id')
    print(videos)
    return render(request, 'web/video.html',{'videos':videos})

def Log_in(request):
    return render(request, 'web/login.html')
    

def Contact(request):
    return render(request,'web/contact.html')


# razorpay
def Subscribe(request):

    plan = request.GET.get('plan', 'monthly')

    if plan == 'yearly':
        amount = "149.00"
        productinfo = "Yearly Subscription"

    elif plan == 'lifetime':
        amount = "299.00"
        productinfo = "Lifetime Subscription"

    else:
        amount = "19.00"
        productinfo = "Monthly Subscription"

    txnid = str(random.randint(1000000, 9999999))

    firstname = "Santosh"
    email = "test@example.com"

    hash_string = (
        f"{settings.PAYU_MERCHANT_KEY}|{txnid}|{amount}|"
        f"{productinfo}|{firstname}|{email}"
        f"|||||||||||{settings.PAYU_SALT}"
    )

    hashh = hashlib.sha512(
        hash_string.encode("utf-8")
    ).hexdigest()

    context = {
        "key": settings.PAYU_MERCHANT_KEY,
        "txnid": txnid,
        "amount": amount,
        "productinfo": productinfo,
        "firstname": firstname,
        "email": email,
        "hashh": hashh,
        "action": settings.PAYU_BASE_URL,
        "plan": plan,
    }

    return render(request, "web/payment.html", context)
def Payment_Success(request):

    status = request.POST.get("status")

    if status == "success":
        return render(
            request,
            "web/payment_success.html"
        )

    return render(
        request,
        "web/payment_sucess.html"
    )


# login / signup
def signup_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # email already exists
        if User.objects.filter(email=email).exists():

            messages.error(request, "Email already exists!")
            return redirect("login")

        # create account
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        messages.success(request, "Account created successfully!")

        return redirect("login")

    return redirect("login")

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        print("USERNAME =", username)
        print("PASSWORD =", password)

        user = authenticate(
            request,
            username=username,
            password=password
        )

        print("USER =", user)

        if user is not None:
            login(request, user)
            return redirect("home")

        messages.error(request, "Invalid username or password")
        return redirect("login")
def user_logout(request):
    logout(request)
    return redirect("home")