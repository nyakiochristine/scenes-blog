from django.shortcuts import render,redirect
from blogpost.models import Post,BlogComment
from django.contrib import messages
from django.views import generic
from django.views.generic import ListView,DetailView
# Create your views here.


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'bloghome.html'

def home(request, *args, **kwargs):
    return render(request, 'bloghome.html', {args: kwargs})



    
    
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
    
    
    
    