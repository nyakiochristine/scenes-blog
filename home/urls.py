from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns=[
    path('',views.home,name='home'),
    
    path('register/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('about/',views.about,name='about'),
    path('images/', views.image,name='images'),
    path('contact/',views.contact,name='contact'),
    path('search/',views.search,name='search'),
    
]