from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register("Usermodel",views.UserViewApi)
router.register("BlogUsermodel",views.BlogUserApi)
router.register("BlogPostmodel",views.BlogPostApi)
router.register("Commentsmodel",views.CommentsApi)
urlpatterns = [
    path('',include(router.urls)),
     path('login/', views.LoginApi.as_view(), name='login'),
     path('logout/', views.LogoutView.as_view(), name='logout'),
     path('search/', views.SearchView.as_view(), name='search'),
]   