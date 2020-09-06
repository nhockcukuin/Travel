from django.urls import path
from . import views

urlpatterns = [
    path("overview/",views.overview,name="overview"),
    path("manage_user",views.manageUser,name="manage_user"),
    path("post/",views.posts,name="posts"),
    path("comments",views.comments,name="comments"),
    path("statistical",views.statistical,name="statistical"),

    path("create_post/",views.createPost,name="create_post"),
    path("edit_post/<str:pk>/",views.editPost,name="update_post"),
    path("delete_post/<str:pk>/",views.deletePost,name="delete_post"),
]
