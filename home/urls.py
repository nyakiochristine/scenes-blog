from django.contrib import admin
from django.urls import path
from home import views

urlpatterns=[
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    
]