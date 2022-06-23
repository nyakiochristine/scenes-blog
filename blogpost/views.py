from django.shortcuts import render,redirect
from blogpost.models import Post,BlogComment
from django.contrib import messages
from django.views import generic
# Create your views here.
def blogHome(request):
    return render(request, 'blogHome.html')

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post_detail.html'





    
    
def blogPost(request):
    return render(request, 'blogpost.html')

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
            
            
    return redirect(f'/blogPost/')
    
    
    
    