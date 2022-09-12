from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main-page'),
    path('posts/', views.posts, name='blog-posts'),
    path('posts/<slug:slug>', views.detailed_post, name='detailed-post') #/posts/my-first-post
]
