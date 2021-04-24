from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):

    STATUS_CHOICES=(("draft","Draft"),("published","Published"))
    title=models.CharField(max_length=350)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog_posts")
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    published_at=models.DateTimeField(datetime.now().date())
    status=models.CharField(choices=STATUS_CHOICES,max_length=10,default="draft")

    objects = models.Manager()  # default manager
    published = PublishedManager()  # custom manager


    class Meta:
        ordering=("-published_at",)

    def __str__(self):
        #return self.title; # this is for admin pannel to show what title
        return f"{self.id} - {self.title} - {self.author}"
        #return str(self.id)+" : "+self.title

