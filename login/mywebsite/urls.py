from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register', views.userregister, name='register'),
    path('login/', views.userlogin, name='login'),
    path('post/<int:id>/', views.readmoreblog, name='readmoreblog'),
    path('profile/', views.userprofile, name='profile'),
    path('addpost/', views.addpost, name='addpost'),
    path('updatepost/<int:id>/', views.updatepost, name='updatepost'),
    path('deletepost/<int:id>/', views.deletepost, name='deletepost'),
    path('blogdashboard/', views.blogdashboard, name='blogdashboard'),
    path('userdashboard/<int:id>/', views.userdashboard, name='userdashboard'),
    path('changepassword1/', views.changepassword1, name='changepassword1'),
    path('changepassword2/', views.changepassword2, name='changepassword2'),
    path('logout/', views.userlogout, name='logout'),

]