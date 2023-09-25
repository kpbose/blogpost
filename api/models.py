from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BlogUser(models.Model):
    username=models.ForeignKey(User,related_name="myname",on_delete=models.CASCADE, null=True,blank=True)
    bio=models.CharField(max_length=30,null=True,blank=True)
    profile=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.username.username

class BlogPost(models.Model):
    sender=models.ForeignKey(User,related_name="posts",on_delete=models.CASCADE, null=True,blank=True)
    blogfile=models.ImageField(null=True,blank=True)
    title=models.CharField(max_length=30,null=True,blank=True)
    content=models.CharField(max_length=1000,null=True,blank=True)
    category=models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.title
    
class Comments(models.Model):
    post=models.ForeignKey(BlogPost,related_name="comments",on_delete=models.CASCADE, null=True,blank=True)
    comment=models.CharField(max_length=100,blank=True,null=True)
    user=models.ForeignKey(User,related_name="commentsby",on_delete=models.CASCADE, null=True,blank=True)
    
    def __str__(self):
        return self.comment