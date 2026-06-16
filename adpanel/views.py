from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Asset

from .models import Template , Video , Motion

# rating user
from .models import Asset, AssetRating
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'ad/index.html')
# upload 
def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None and user.is_superuser:
            login(request, user)
            messages.success(
                request,
                "Admin Login Successful"
            )
            return redirect("home")
        messages.error(
            request,
            "Invalid Admin Credentials"
        )
        return redirect("admin_login")
    return render(
request, "ad/admin_login.html")

def upload_template(request):
    if request.method == "POST":
        Template.objects.create(
            title=request.POST.get("title"),
            category=request.POST.get("category"),
            price=request.POST.get("price"),
            rating=request.POST.get("rating"),
            downloads=request.POST.get("downloads"),
            badge=request.POST.get("badge"),
            image=request.FILES.get("image"),
            description=request.POST.get("description"))
        return redirect("upload_template")
    templates = Template.objects.all().order_by('-id')
    return render(request, "ad/upload_template.html",  {"templates": templates})
def delete_template(request, id):
    template = Template.objects.get(id=id)
    template.delete()
    return redirect("upload_template")
def edit_template(request, id):
    template = Template.objects.get(id=id)

    if request.method == "POST":
        print("UPDATE BUTTON CLICKED")
        template.title = request.POST.get("title")
        template.category = request.POST.get("category")
        template.price = request.POST.get("price")
        template.rating = request.POST.get("rating")
        template.downloads = request.POST.get("downloads")
        template.badge = request.POST.get("badge")
        template.description = request.POST.get("description")

        if request.FILES.get("image"):
            template.image = request.FILES.get("image")

        template.save()

        return redirect("upload_template")

    return render(request, "ad/edit_template.html", {"template": template})

def upload_video(request):
    if request.method == "POST":
        Video.objects.create(
            title=request.POST.get("title"),
            category=request.POST.get("category"),
            price=request.POST.get("price"),
            rating=request.POST.get("rating"),
            downloads=request.POST.get("downloads"),
            badge=request.POST.get("badge"),
            thumbnail=request.FILES.get("thumbnail"),
            video=request.FILES.get("video"))
        return redirect("upload_video")
    videos = Video.objects.all().order_by('-id')
    return render(request,'ad/upload_video.html', {'videos': videos}    )

def delete_video(request, id):
    video = Video.objects.get(id=id)
    video.delete()
    return redirect("upload_video")

def edit_video(request, id):
    video = Video.objects.get(id=id)
    if request.method == "POST":
        video.title = request.POST.get("title")
        video.category = request.POST.get("category")
        video.price = request.POST.get("price")
        video.rating = request.POST.get("rating")
        video.downloads = request.POST.get("downloads")
        video.badge = request.POST.get("badge")
        video.description = request.POST.get("description")
        if request.FILES.get("thumbnail"):
            video.thumbnail = request.FILES.get("thumbnail")
        if request.FILES.get("video"):
            video.video = request.FILES.get("video")
        video.save()
        return redirect("upload_video")
    return render(request, "ad/edit_video.html",{"video": video})


def upload_motion(request):

    if request.method == "POST":

        Motion.objects.create(
            title=request.POST.get("title"),
            category=request.POST.get("category"),
            price=request.POST.get("price"),
            rating=request.POST.get("rating"),
            downloads=request.POST.get("downloads"),
            badge=request.POST.get("badge"),
            thumbnail=request.FILES.get("thumbnail"),
            video=request.FILES.get("video"),
            description=request.POST.get("description")
        )

        return redirect("upload_motion")

    motions = Motion.objects.all().order_by('-id')

    return render(
        request,
        'ad/upload_motion.html',
        {'motions': motions}
    )
def delete_motion(request, id):

    motion = Motion.objects.get(id=id)

    motion.delete()

    return redirect("upload_motion")
def edit_motion(request, id):

    motion = Motion.objects.get(id=id)

    if request.method == "POST":

        motion.title = request.POST.get("title")
        motion.category = request.POST.get("category")
        motion.price = request.POST.get("price")
        motion.rating = request.POST.get("rating")
        motion.downloads = request.POST.get("downloads")
        motion.badge = request.POST.get("badge")
        motion.description = request.POST.get("description")

        if request.FILES.get("thumbnail"):
            motion.thumbnail = request.FILES.get("thumbnail")

        if request.FILES.get("video"):
            motion.video = request.FILES.get("video")

        motion.save()

        return redirect("upload_motion")

    return render(
        request,
        "ad/edit_motion.html",
        {"motion": motion}
    )



# upload
def upload_asset(request):

    if request.method == "POST":

        Asset.objects.create(
    asset_type=request.POST.get("asset_type"),
    title=request.POST.get("title"),
    category=request.POST.get("category"),
    price=request.POST.get("price") or 0,
    downloads=request.POST.get("downloads") or 0,
    badge=request.POST.get("badge"),
    description=request.POST.get("description"),
    thumbnail=request.FILES.get("thumbnail"),
    preview_video=request.FILES.get("preview_video"),
    zip_file=request.FILES.get("zip_file")
)

        return redirect("upload_asset")

    assets = Asset.objects.all().order_by("-id")

    return render(
        request,
        "ad/upload_asset.html",
        {
            "assets": assets
        }
    )
def edit_asset(request, id):

    asset = Asset.objects.get(id=id)

    if request.method == "POST":

        asset.asset_type = request.POST.get("asset_type")
        asset.title = request.POST.get("title")
        asset.category = request.POST.get("category")
        asset.price = request.POST.get("price")
        asset.downloads = request.POST.get("downloads")
        asset.badge = request.POST.get("badge")
        asset.description = request.POST.get("description")

        if request.FILES.get("thumbnail"):
            asset.thumbnail = request.FILES.get("thumbnail")

        if request.FILES.get("preview_video"):
            asset.preview_video = request.FILES.get("preview_video")

        if request.FILES.get("zip_file"):
            asset.zip_file = request.FILES.get("zip_file")

        asset.save()

        return redirect("upload_asset")

    return render(
        request,
        "ad/edit_asset.html",
        {
            "asset": asset
        }
    )
def delete_asset(request, id):

    asset = Asset.objects.get(id=id)

    asset.delete()

    return redirect("upload_asset")
