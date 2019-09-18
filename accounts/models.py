from django.db import models
from django.db.models.signals import post_save


# Create your models here.

class Signup(models.Model):
    username =models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password =models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user =models.OneToOneField(Signup, on_delete=models.CASCADE)
    full_name=models.CharField(max_length=100)
    dob= models.CharField(max_length=10)
    city=models.CharField(max_length=50)
    pic =models.ImageField(upload_to='profile', default='pr.png')
    status =models.CharField(max_length=200)

    def __str__(self):
        return self.user.username




def create_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_profile,sender=Signup)




