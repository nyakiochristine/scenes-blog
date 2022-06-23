from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    
    path('home/', views.PostList.as_view(), name='home'),
    path('blogHome/',views.blogHome,name='BlogHome'),
    path(r'<pk>postdetail/', views.PostDetail.as_view(), name='post_detail'),
    path(r'blogpost/',views.blogPost,name='blogPost'),
    path('postComment/',views.postComment,name='postComment'),
]