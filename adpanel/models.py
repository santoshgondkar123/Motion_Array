from django.db import models
from django.contrib.auth.models import User
class Template(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    rating = models.FloatField(default=0)
    downloads = models.IntegerField(default=0)
    badge = models.CharField(max_length=50)
    image = models.ImageField(upload_to='templates/')
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Video(models.Model):

    title = models.CharField(max_length=200)

    category = models.CharField(max_length=100)

    price = models.IntegerField()

    rating = models.FloatField(default=0)

    downloads = models.IntegerField(default=0)

    badge = models.CharField(max_length=100)

    thumbnail = models.ImageField(
        upload_to='videos/thumbnails/'
    )

    video = models.FileField(
        upload_to='videos/files/'
    )

    def __str__(self):
        return self.title
    
class Motion(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    rating = models.CharField(max_length=20)
    downloads = models.CharField(max_length=50)
    badge = models.CharField(max_length=50)

    thumbnail = models.ImageField(
        upload_to='motion/thumbnails/'
    )

    video = models.FileField(
        upload_to='motion/videos/'
    )

    description = models.TextField()

    def __str__(self):
        return self.title



class Asset(models.Model):

    ASSET_TYPES = (
        ('template', 'Template'),
        ('video', 'Video'),
        ('motion', 'Motion Graphics'),
    )

    asset_type = models.CharField(
        max_length=20,
        choices=ASSET_TYPES
    )

    title = models.CharField(
        max_length=200
    )

    category = models.CharField(
        max_length=100
    )

    price = models.IntegerField(
        default=0
    )

    total_rating = models.IntegerField(default=0)

    rating_count = models.IntegerField(default=0)
    downloads = models.IntegerField(
        default=0
    )

    badge = models.CharField(
        max_length=100,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    thumbnail = models.ImageField(
        upload_to='assets/thumbnails/',
        blank=True,
        null=True
    )

    preview_video = models.FileField(
        upload_to='assets/previews/',
        blank=True,
        null=True
    )

    zip_file = models.FileField(
        upload_to='assets/zips/'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.title} ({self.asset_type})"





class AssetRating(models.Model):
    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
        related_name='ratings'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField()

    class Meta:
        unique_together = ('asset', 'user')

    def __str__(self):
        return f"{self.user.username} - {self.asset.title}"


class Subscription(models.Model):

    PLAN_CHOICES = (
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
        ('lifetime', 'Lifetime'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    plan = models.CharField(
        max_length=20,
        choices=PLAN_CHOICES
    )

    is_active = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.plan}"