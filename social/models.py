from ast import Str
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from landing.models import Post, Profile

# class Post(models.Model):
#     body = models.TextField()
#     created_on = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)


# class Comment(models.Model):
#     sno = models.AutoField(primary_key= True, default='0')
#     comment = models.TextField(blank=True)
#     created_on = models.DateTimeField(default=timezone.now)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.comment[0:5] + "by " + self.auther
class Comment(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.comment


class stori(models.Model):
    story_user = models.ForeignKey(Profile, on_delete= models.CASCADE,related_name='story_post')
    image = models.ImageField( upload_to='story_pics')
    posted_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.story_user
    

