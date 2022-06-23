import email
import re
from home.models import Contact
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from blogpost.models import Post
# Create your views here.
def home(request):
    return render(request, 'home.html')
    

def contact(request):
    if request.method == 'POST':
        name= request.POST['name']
        email= request.POST['email']
        roll= request.POST['roll']
        content= request.POST['content']
        print(name,email,roll,content)
        
        if len(name)< 2 or len(roll)<5  or len(email)<2:
            messages.error(request,'Please fill the form correctly')
        
        else:
            contact = Contact(name=name,email=email,roll=roll,content=content)
            contact.save()
            messages.success(request,'Success! Your response has been recorded')
    return render(request,'contact.html')


def handleSignup(request):
    if request.method == 'POST':
        username= request.POST['username']
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']
        
        
        if len(username)>15:
            messages.error(request, 'Your Username must be at least 15 characters')
            return redirect('home')
        if not username.isalnum():
            messages.error(request, 'username should only contain alphabetic and alphanumeric characters')
            return redirect('home')
        
        if pass1 != pass2:
            messages.success(request, 'Confirm password does not match')
            return redirect('home')
        
        #create the user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request, 'Your account has been successfully created.')
        return redirect('home')
    
    else:
        return HttpResponse('404 Not Found')


def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        
        user = authenticate(username=loginusername, password=loginpassword)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('home')
    return HttpResponse('404 Not Found')

def handleLogout(request):
    logout(request)
    messages.success(request, 'Logout successfully')
    return redirect('home')


def search(request):
    query= request.GET['query']
    if len(query)>78:
        allPosts = Post.objects.none()
        
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPosts= allPostsTitle.union(allPostsAuthor)
        
    if allPosts.count() == 0:
        messages.warning(request, "No posts found")
    params={"allPosts": allPosts,"query": query}
    return render(request,'search.html',params=params)
        
        
    
