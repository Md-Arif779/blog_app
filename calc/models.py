from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True,upload_to="images/profile/")
    website_url = models.CharField(max_length=300, null=True, blank=True)
    facebook_url = models.CharField(max_length=300, null=True, blank=True)
    twitter_url = models.CharField(max_length=300, null=True, blank=True)
    instagram_url = models.CharField(max_length=300, null=True, blank=True)
    pinterest_url = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('home')
    

class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    post_image = models.ImageField(null=True, blank=True, upload_to="images/")
    category = models.CharField(max_length=300, default='coding')
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home')
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)    
