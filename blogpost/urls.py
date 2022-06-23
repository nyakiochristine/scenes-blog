from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('',views.blogHome,name='BlogHome'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('postComment',views.postComment,name='postComment'),
    

]