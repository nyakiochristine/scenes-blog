import email
from unicodedata import name
from xmlrpc.client import DateTime
from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name= models.CharField(max_length=55)
    email= models.EmailField(max_length=105, blank=True)
    roll=models.CharField(max_length=15)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True, blank=True)
    
    
    def __str__(self):
        return 'Submitted by' +self.name
    