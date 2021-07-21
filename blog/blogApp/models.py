from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    date_posted = models.DateTimeField(default=timezone.now) 
    #takes our timezone settings into consideration *Don't put parantheses after now*

    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    #CASCADE: when user is deleted their post also will be deleted
    #one to many relationship, thats why we use Foreignkey in django

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})


 