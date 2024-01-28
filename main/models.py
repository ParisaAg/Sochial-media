from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
from django.core.validators import FileExtensionValidator
import uuid
# Create your models here.
User= get_user_model()
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio= models.TextField(blank=True)
    pro_photo = models.ImageField(upload_to='profilephotos',default='blank-mages.png')

    def __str__(self):
        return self.user.username







class Post(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.CharField(max_length=100)
    content = models.ImageField(upload_to='postsimg')
    captions = models.TextField(max_length=120)
    created_at = models.DateTimeField(default=datetime.now)
    no_likes = models.IntegerField(default=0)
    video = models.FileField(upload_to='videos_uploaded', null=True,
    validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])

    def __str__(self):
        return self.user


class Like(models.Model):
    post_id=models.CharField(max_length=600)
    username=models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Followers(models.Model):
    follower=models.CharField(max_length=100)
    user=models.CharField(max_length=100)

    def __str__(self):
        return self.user