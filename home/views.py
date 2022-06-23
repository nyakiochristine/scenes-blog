from home.models import Contact
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home/home.html')
    

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
    return render(request,'home/contact.html')
