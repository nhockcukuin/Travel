from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    sub_category = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.sub_category
    

class Posts(models.Model):
    title = models.CharField(max_length=255,null=True)
    category = models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    img_post = models.ImageField(null=True)
    content = models.TextField(null=True)
    date_create = models.DateField(auto_now_add=True,null=True)
    date_update = models.DateField(auto_now=True,null=True)
    active = models.BooleanField(default=False)
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    #slug
    def __str__(self):
        return self.title
    

#class Comment(models.Model)
