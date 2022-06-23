from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('postComment',views.postComment,name='postComment'),
    path('BlogHome',views.blogHome,name='BlogHome'),
    path('<str:slug>',views.blogPost,name='blogPost'),

]