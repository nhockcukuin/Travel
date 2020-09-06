from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PostForm


from .models import *
# Create your views here.


# Tong quan
def overview(request):
    return render(request,"pages/overview.html")

#Quan ly nguoi dung
def manageUser(request):
    return render(request,"pages/manage_user.html")

#Bai viet
def posts(request):
    posts = Posts.objects.all()
    context = {'posts':posts}
    return render(request,"pages/posts.html",context)
#Binh luan
def comments(request):
    return render(request,"pages/comments.html")

#Thong ke
def statistical(request):
    return render(request,"pages/statistical.html")

#Tao bai viet
def createPost(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
        return redirect('posts')
    context = {'form': form}
    return render(request,'pages/create_post.html',context)

#Sua bai viet
def editPost(request,pk):
    post = Posts.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid:
            form.save()
        return redirect('posts')
    context = {'form':form}
    return render(request,'pages/create_post.html',context)

#Xóa bài viết
def deletePost(request,pk):
    post = Posts.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect('posts')
    context = {'item':post}
    return render(request,'pages/delete_post.html',context)