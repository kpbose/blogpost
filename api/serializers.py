from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.reverse import reverse

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields="__all__"

class BlogPostSerializer(serializers.ModelSerializer):
    comments=CommentsSerializer(read_only=True,many=True)
    class Meta:
        model=BlogPost
        fields=['sender','blogfile','title','category','content','comments','url']
class BlogUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogUser
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    myname=BlogUserSerializer(read_only=True,many=True)
    commentsby=CommentsSerializer(read_only=True,many=True)
    posts=BlogPostSerializer(read_only=True,many=True)
    class Meta:
        model=User
        fields=['username','first_name','last_name','password','email','myname','commentsby','posts','url']

class LoginSerializer(serializers.Serializer):
     username=serializers.CharField()
     password=serializers.CharField()
     

class LogoutSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=100, default="Logout successful")
