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
from adpanel.models import Asset
from django.db.models import Avg, Count
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from adpanel.models import Subscription
from adpanel.models import AssetRating
# from django.contrib.auth.decorators import login_required
from adpanel.models import Asset, AssetRating
def Home(request):
    from django.contrib.auth import get_user_model

    User = get_user_model()

    if not User.objects.filter(username="Templates").exists():
        User.objects.create_superuser(
            username="Templates",
            email="santoshgondkar22@gmail.com",
            password="santosh@123"
        )
    return render(request, 'web/base.html')
def Template(request):

    templates = Asset.objects.filter(
        asset_type='template'
    ).annotate(
        average_rating=Avg('ratings__rating'),
        total_reviews=Count('ratings')
    ).order_by('-id')

    for item in templates:

        item.user_rating = 0

        if request.user.is_authenticated:

            rating = item.ratings.filter(
                user=request.user
            ).first()

            if rating:
                item.user_rating = rating.rating

    return render(
        request,
        'web/template.html',
        {
            'templates': templates
        }
    )
def Motion_graphics(request):

    motions = Asset.objects.filter(
        asset_type='motion'
    ).annotate(
        average_rating=Avg('ratings__rating'),
        total_reviews=Count('ratings')
    ).order_by('-id')

    for item in motions:

        item.user_rating = 0

        if request.user.is_authenticated:

            rating = item.ratings.filter(
                user=request.user
            ).first()

            if rating:
                item.user_rating = rating.rating

    return render(
        request,
        'web/motion_graphics.html',
        {
            'motions': motions
        }
    )

def Video(request):

    videos = Asset.objects.filter(
        asset_type='video'
    ).annotate(
        average_rating=Avg('ratings__rating'),
        total_reviews=Count('ratings')
    ).order_by('-id')

    for item in videos:

        item.user_rating = request.session.get(
        f"rated_asset_{item.id}",
        0
    )

    return render(
        request,
        'web/video.html',
        {
            'videos': videos
        }
    )
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

        if request.user.is_authenticated:

            plan = request.POST.get(
                "productinfo",
                "Monthly Subscription"
            )

            if "Yearly" in plan:
                selected_plan = "yearly"

            elif "Lifetime" in plan:
                selected_plan = "lifetime"

            else:
                selected_plan = "monthly"

            subscription, created = Subscription.objects.get_or_create(
                user=request.user
            )

            subscription.plan = selected_plan
            subscription.is_active = True
            subscription.save()

        return render(
            request,
            "web/payment_success.html"
        )

    return render(
        request,
        "web/payment_failed.html"
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

def download_asset(request, id):

    if not request.user.is_authenticated:
        return redirect("login")

    has_subscription = Subscription.objects.filter(
        user=request.user,
        is_active=True
    ).exists()

    if not has_subscription:
        return redirect("subscribe")

    asset = get_object_or_404(
        Asset,
        id=id
    )

    return FileResponse(
        asset.zip_file.open('rb'),
        as_attachment=True,
        filename=asset.zip_file.name.split('/')[-1]
    )

def rate_asset(request, id):

    asset = Asset.objects.get(id=id)

    rating = int(request.POST.get("rating"))

    if 1 <= rating <= 5:

        if request.user.is_authenticated:

            AssetRating.objects.update_or_create(
                asset=asset,
                user=request.user,
                defaults={
                    "rating": rating
                }
            )

        else:

            guest_ip = request.META.get("REMOTE_ADDR")

            AssetRating.objects.update_or_create(
                asset=asset,
                guest_ip=guest_ip,
                defaults={
                    "rating": rating,
                    "user": None
                }
            )

    return redirect(
        request.META.get("HTTP_REFERER", "/")
    )