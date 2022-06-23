from django.shortcuts import render,redirect
from blogpost.models import Post,BlogComment
from django.contrib import messages
# Create your views here.
def blogHome(request):
    return render(request, 'index.html')
    
    
def blogPost(request):
    return render(request, 'post.html')

def postComment(request):
    if request.method == 'POST':
        comment= request.POST.get('comment'),
        user=request.user
        postSno=request.POST.get('postSno')
        post=Post.objects.get(sno=postSno)
        parentSno=request.POST.get('parentSno')
        if parentSno == '':
            comment= BlogComment(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request, 'Yourcomment has been saved successfully.')
            
            
    return redirect(f'/blog/{post.slug}')
    
    
    
    