from django import forms
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UserChangeForm
from django.contrib.auth.models import User
from .models import BlogPost, Connectus
from django.utils.translation import gettext, gettext_lazy as _
# from ckeditor_uploader.widgets import CKEditorWidget, CKEditorUploadingWidget
# from ckeditor.widgets import CKEditorWidget , CKEditorUploadingWidget
from ckeditor_uploader.fields import RichTextUploadingField


class BlogPostForm(forms.ModelForm):
    # updated =  forms.DateTimeField(label='Updated On', widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
    # created = forms.DateTimeField(label='Created On', widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
    class Meta:
         model = BlogPost
         fields = ['title', 'author', 'blog_post']
         labels = {'title': 'Title', 'blog_post':'Blog Post'}
         widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                    'author' : forms.Select(attrs={'class': 'form-control, justify-text'}),
                    'blog_post' : forms.CharField(widget=RichTextUploadingField()),
                   }

class ConnectusForm(forms.ModelForm):
    class Meta:
        model = Connectus
        fields = ['fname','mname','lname','address','mobile','subject','message']
        labels = {'fname': 'First Name', 'mname':'Middel Name', 'lname':'Last Name',
                  'address':'Permanent Address', 'mobile':'Mobile','subject':'Subject',
                  'message':'Message'}
        widgets = {'fname': forms.TextInput(attrs={'class': 'form-control'}),
                   'mname': forms.TextInput(attrs={'class': 'form-control'}),
                   'lname': forms.TextInput(attrs={'class': 'form-control'}),
                   'address': forms.TextInput(attrs={'class': 'form-control'}),
                   'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
                   'subject': forms.TextInput(attrs={'class': 'form-control'}),
                   'message': forms.Textarea(attrs={'class': 'form-control'}),
                }

class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login', 'date_joined',
                  'last_login']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email',
                  'date_joined': 'Date of Joined', 'last_login': 'Last Login'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'date_joined': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_login': forms.TextInput(attrs={'class': 'form-control'}),
                   }


class AdminProfileForm(UserChangeForm):
    password = None
    is_superuser = forms.BooleanField(label='Is Superuser', widget=forms.CheckboxInput(attrs={'class': ''}))
    is_staff = forms.BooleanField(label='Is Staff', widget=forms.CheckboxInput(attrs={'class': ''}))
    is_active = forms.BooleanField(label='Is Active', widget=forms.CheckboxInput(attrs={'class': ''}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_superuser', 'groups', 'user_permissions',
                  'is_staff', 'is_active', 'date_joined', 'last_login', ]
        labels = {'username': 'Username', 'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email',
                  'is_superuser': 'Is Superuser', 'groups': 'Groups', 'user_permissions': 'User Permissions',
                  'is_staff': 'Is Staff', 'is_active': 'Is Active', 'date_joined': 'Date of Joined',
                  'last_login': 'Last Login'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'last_login': forms.TextInput(attrs={'class': 'form-control'}),
                   'date_joined': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_login': forms.TextInput(attrs={'class': 'form-control'}),
                   'user_permissions' : forms.CheckboxSelectMultiple(attrs={'class': 'form-control, justify-text'}),
                   'groups' : forms.CheckboxSelectMultiple(attrs={'class': 'form-control, justify-text'}),
                   }


class PasswordChangeOne(PasswordChangeForm):
    old_password = forms.CharField(label='Enter Old Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='Enter New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Re-Enter New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['old_password','new_password1', 'new_password2']
        labels = {'old_password':'Old Password','new_password1':'Enter New Password', 'new_password1':'Re-Enter New Password'}
       

class PasswordChangeTwo(SetPasswordForm):
    new_password1 = forms.CharField(label='Enter New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Re-Enter New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']
        labels = {'new_password1':'Enter New Password', 'new_password1':'Re-Enter New Password'}



        