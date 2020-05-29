from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(blank=False,null=False,max_length=40)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField(blank=False,null=False)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post-detail',kwargs={'pk':self.pk})