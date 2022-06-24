from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Post(models.Model):
    title=  models.CharField(max_length=255, unique=True),
    slug = models.SlugField(max_length=200),
    author=  models.CharField(max_length=255, unique=True),
    content=  models.TextField()
    updated_on = models.DateTimeField(auto_now= True)
    images= models.ImageField(upload_to='images',default='default.png')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    def __str__(self):
        return self.content 
    
    
    class Meta:
            ordering = ['-created_on']

    
    
    
    
    
class BlogComment(models.Model):
    comment=  models.TextField(max_length=255, blank=True),
    user= models.ForeignKey(User, blank=True,on_delete=models.CASCADE)
    post=  models.ForeignKey(Post, blank=True,on_delete = models.CASCADE)