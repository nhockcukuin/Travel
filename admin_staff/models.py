from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Category(models.Model):
    sub_category = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.sub_category
    

class Posts(models.Model):
    title = models.CharField(max_length=255,null=True)
    category = models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    img_post = models.ImageField(null=True)
    content = RichTextUploadingField(null=True)
    date_create = models.DateField(auto_now_add=True,null=True)
    date_update = models.DateField(auto_now=True,null=True)
    active = models.BooleanField(default=False)
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    #slug
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Posts,null=False,on_delete=models.CASCADE)
    user_cmt = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    content_cmt = models.TextField(null=True)

class Handbook(models.Model):
    title_hb = models.CharField(max_length=255)
    img_hb = models.ImageField(null=True)
    content_hb = models.TextField(null=True)
    date_cr = models.DateField(auto_now_add=True)
    date_up = models.DateField(auto_now=True)
    active = models.BooleanField(default=False)
    user_cr = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    #slug_db