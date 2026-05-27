from django.conf import settings

from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
import hashlib
import random
# Create your views here.

def Home(request):
    return render(request, 'web/base.html')

def Template(request):
    return render(request,'web/template.html')

# def Video_Template(request):
#     return render(request, 'web/video_template.html')

def Motion_graphics(request):
    return render(request ,'web/motion_graphics.html')

def Video(request):
    return render(request, 'web/video.html')

def Log_in(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        # Demo Login
        if email and password:

            messages.success(
                request,
                "Login Successful!"
            )

            return redirect('web/payment.html')

        else:

            messages.error(
                request,
                "Invalid Credentials"
            )

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
