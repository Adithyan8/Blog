from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) #user deleted implies profile deleted
    image = models.ImageField(default = 'default.jpg')
    
    def __str__(self):
        return f"{self.user.username} Profile"
    