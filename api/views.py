
from django.contrib.auth.models import User

from .serializers import *
from .models  import *
from django.contrib.auth import authenticate, login,logout
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status

class SearchView(APIView):
    def post(self,request):
        data=request.data
        queryset=BlogPost.objects.filter(category=data['category']).values('sender','blogfile','title','category','content')
        dict={
            'blogpost': []
        }
        for i in queryset:
            dict['blogpost'].append(i)
    
        if len(queryset)==0:
            msg={"message":"Category not found"}
            return Response(
               msg,status=status.HTTP_201_CREATED
             )
        return Response(
               dict,status=status.HTTP_201_CREATED
        )
class LogoutView(APIView):
    def get(self, request):
        serializer = LogoutSerializer(data={'message': 'Logout successful'})
        if serializer.is_valid():
            logout(request)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginApi(APIView):
    def post(self,request):
        print("1")
        try:
            data=request.data
            serializer=LoginSerializer(data=data)
            if serializer.is_valid():
             email=serializer.data['username']
             password=serializer.data['password']
             print(email,password)
             user=authenticate(username=email,password=password)
             if user is None:
                    return Response({
                             'status':400,
                        'message':'Invalid Credentials',
                            'data':{} 
                    })
             login(request,user)
             return Response({
                  'message':'Login Successful',
                  'username': str(email),
                 })
            
            return Response({
                'status':400,
                'message':'something went wrong',
                'data':{}
            })  
        except Exception as e:
            print(e)
class UserViewApi(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class BlogUserApi(viewsets.ModelViewSet):
    queryset=BlogUser.objects.all()
    serializer_class=BlogUserSerializer

class BlogPostApi(viewsets.ModelViewSet):
    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer

class CommentsApi(viewsets.ModelViewSet):
    queryset=Comments.objects.all()
    serializer_class=CommentsSerializer