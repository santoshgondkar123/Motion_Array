from django.db import models

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