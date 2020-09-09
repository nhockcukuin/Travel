from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import PostForm,UserForm

from .filters import PostFilter
from .models import *
# Create your views here.


# Tong quan
def overview(request):
    return render(request,"pages/overview.html")

#Quan ly nguoi dung
def manageUser(request):
    user = User.objects.all()
    context = {'user':user}
    return render(request,"pages/manage_user.html",context)

#Bai viet
def posts(request):
    posts = Posts.objects.all()
    postFilter = PostFilter(request.GET, queryset=posts)
    posts = postFilter.qs
    context = {'posts':posts,'postFilter':postFilter}
    return render(request,"pages/posts.html",context)
#Binh luan
def comments(request):
    cmt = Comment.objects.all()
    context = {'cmt':cmt}
    return render(request,"pages/comments.html",context)

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

#Xóa bình luận
def deleteComment(request,pk):
    cmt = Comment.objects.get(id=pk)
    if request.method == "POST":
        cmt.delete()
        return redirect('comments')
    context = {'cmt':cmt}
    return render(request,'pages/delete_cmt.html',context)

#Thông tin tài khoản
def viewUser(request,pk):
    user = User.objects.get(id=pk)
    formUser = UserForm(instance=user)
    if request.method == "POST":
        formUser = UserForm(request.POST,instance=user)
        if formUser.is_valid:
            formUser.save()
        return redirect('manage_user')
    context = {'formUser':formUser}
    return render(request,'pages/view_user.html',context)