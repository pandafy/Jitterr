from django.db import models
from accounts.models import FrontendUsers
from django.utils import timezone

# Create your models here.
class Jit(models.Model):
    value = models.CharField(max_length = 100, blank = False)
    author = models.ForeignKey(FrontendUsers, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now() )
    is_reply = models.BooleanField(default=False)
    likes = models.IntegerField(blank=False,default=0)

    def __str__(self):
        return self.value

class Jit_Likedby(models.Model):
    jit_id = models.ForeignKey(Jit,blank = False, on_delete= models.CASCADE)
    user_id = models.ForeignKey(FrontendUsers,blank = False,on_delete= models.CASCADE)

class Jit_Comment(models.Model):
    parent_id = models.ForeignKey(Jit,blank = False, on_delete = models.CASCADE)
    comment_id = models.ForeignKey(Jit,blank = False, on_delete = models.CASCADE, related_name='comment')


    