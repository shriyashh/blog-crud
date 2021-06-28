from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    blog_post = RichTextUploadingField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)

        
class Connectus(models.Model):
    fname = models.CharField(max_length=150)
    mname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    address = models.TextField(max_length=150)
    mobile = models.CharField(max_length=10)
    subject = models.TextField(max_length=150)
    message = models.CharField(max_length=150)




