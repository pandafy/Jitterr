from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class users(User):
    pass

class FrontendUsers(users):
    users.username = models.TextField(max_length=30,null=False,primary_key=True)
    bio = models.TextField(max_length=200,blank=True)
    avatar = models.ImageField(upload_to = 'media/media')

class Followers(models.Model):
    follower = models.ForeignKey(FrontendUsers,on_delete=models.CASCADE,related_name='follower')
    following = models.ForeignKey(FrontendUsers,on_delete=models.CASCADE,related_name='following')