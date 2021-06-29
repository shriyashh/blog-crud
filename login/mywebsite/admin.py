from django.contrib import admin
from .models import BlogPost, Connectus, CommentOnPost

admin.site.register(BlogPost)
class BlogPostModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','blog_post','updated','created','likes']

admin.site.register(CommentOnPost)
class CommentOnPostModelAdmin(admin.ModelAdmin):
    list_display = ['id','post','name','body']


admin.site.register(Connectus)
class ConnectusModelAdmin(admin.ModelAdmin):
    list_display = ['id','fname','mname','lname','address','mobile','subject','message']
