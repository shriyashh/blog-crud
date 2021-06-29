from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import SignupForm, LoginForm, PasswordChangeOne, PasswordChangeTwo
from .forms import UserProfileForm, AdminProfileForm
from .forms import BlogPostForm, ConnectusForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm, SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .models import BlogPost
from django.contrib.auth.models import Group
from django.urls import reverse

# Create your views here.
def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'index.html', {'posts': posts})

def readmoreblog(request, id):
    if request.user.is_authenticated:
        post = BlogPost.objects.get(pk=id) 
        blogpostlikes = post.blogpostlikes()
        liked = False
        if blogpostlikes.likes.filter(id=request.user.id).exists():
            liked = True
            return render(request, 'readmoreblog.html', {'post': post, 'blogpostlikes':blogpostlikes, 'liked':liked })
    else:
        return HttpResponseRedirect('/login/')

def likes(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(BlogPost, id=request.POST.get('post_id'))
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True
        return HttpResponseRedirect(reverse('readmoreblog', args=[str(id)]))
    else:
        return HttpResponseRedirect('/login/')

def userregister(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            messages.success(request, 'Success!!')
            return HttpResponseRedirect('/login/')

    else:
        form = SignupForm()
    return render(request, 'register.html', {'form': form})


def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                u = form.cleaned_data['username']
                p = form.cleaned_data['password']
                user = authenticate(username=u, password=p)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'logged In!!')
                    return HttpResponseRedirect('/')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')


def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')


def userprofile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                posts = BlogPost.objects.all()
                form = AdminProfileForm(request.POST, instance=request.user)
                users = User.objects.all()
            else:       
                form = UserProfileForm(request.POST, instance=request.user)
                users = None
            if form.is_valid():
                form.save()
        else:
            if request.user.is_superuser == True:
                posts = BlogPost.objects.all()
                form = AdminProfileForm(instance=request.user)
                users = User.objects.all()
            else:
                form = UserProfileForm(instance=request.user)
                users = None
        return render(request, 'profile.html', {'name': request.user.username, 'posts':posts,'form': form, 'users': users})
    else:
        return HttpResponseRedirect('/login/')


def userdashboard(request, id):
    if request.user.is_authenticated:
        dashbordDetails = User.objects.get(pk=id)
        form = AdminProfileForm(instance=dashbordDetails)
        return render(request, 'userdashboard.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')


def changepassword1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeOne(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password Changed!!')
                update_session_auth_hash(request, form.user)
                return HttpResponseRedirect('/profile/')
        else:
            form = PasswordChangeOne(user=request.user)
        return render(request, 'changepassword1.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')


def changepassword2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeTwo(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password Changed!!')
                update_session_auth_hash(request, form.user)
                return HttpResponseRedirect('/profile/')
        else:
            form = PasswordChangeTwo(user=request.user)
        return render(request, 'changepassword2.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')


def blogdashboard(request):
    if request.user.is_authenticated:
        user = request.user
        posts = BlogPost.objects.filter(author=user)
        return render(request, 'blogdashboard.html', {'posts': posts})
    else:
        return HttpResponseRedirect('/login/')


def addpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BlogPostForm(request.POST)
            if form.is_valid():
                form.save()
                form = BlogPostForm()
        else:
            form = BlogPostForm()    
        return render(request, 'addpost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')


def updatepost(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            updatedPost = BlogPost.objects.get(pk=id)
            form = BlogPostForm(request.POST, instance=updatedPost)
            if form.is_valid():
                form.save()
        else:
            updatedPost = BlogPost.objects.get(pk=id)
            form = BlogPostForm(instance=updatedPost)
        return render(request, 'updatepost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')


def deletepost(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            updatedPost = BlogPost.objects.get(pk=id)
            updatedPost.delete()
        return HttpResponseRedirect('/blogdashboard/')
    else:
        return HttpResponseRedirect('/login/')

