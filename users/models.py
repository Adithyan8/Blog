from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) #user deleted implies profile deleted
    image = models.ImageField(default = 'default.png',upload_to='media')
    
    def __str__(self):
        return f"{self.user.username} Profile"
    
    def save(self,*args,**kwargs):                     #This function to create custom save function
        super().save(*args,**kwargs)
        img=Image.open(self.image.path)
                                                 #used to resize uploaded image to reduce size of the image file
        if img.height>200 or img.width>200 : 
            output_size=(200,200)
            img.thumbnail(output_size)             #resizes the image
            img.save(self.image.path)