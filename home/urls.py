from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings

from django.conf.urls import static
urlpatterns=[
    path('',views.home,name='home'),
    path('account/', include('django.contrib.auth.urls')),
    
    path('register/', views.signup, name='signup'),
    path('about/',views.about,name='about'),
    path('images/', views.image,name='images'),
    path('contact/',views.contact,name='contact'),
    path('search/',views.search,name='search'),
    
]


