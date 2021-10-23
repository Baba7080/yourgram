from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import FieldError
from django.db.models.base import Model
from django.utils.text import slugify
from django.utils import timezone
from django.template.defaultfilters import default, slugify
from django.db.models import Q

from django.shortcuts import reverse

# Create your models here.

STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted')
)
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=20,default='')
    Second_Name = models.CharField(max_length=20,default='')
    bio =models.TextField(blank=True)
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    following = models.ManyToManyField(User, related_name='follwing',blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)
    city = models.CharField(max_length=200,default='city')
    Phone_Number = models.CharField(max_length=10,null=True)
    image = models.ImageField(default='profile_pics/deafault.jpeg', upload_to='profile_pics')
    class Meta:
        ordering = ['-created']


    def __str__(self):
        return f"{self.user.username}"



class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    liked = models.ManyToManyField(User, blank=True, related_name='likes', default=None)
    # slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    image = models.ImageField( upload_to='Post_pics')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def num_likes(self):
        return self.liked.all().count()
    def count_posts_of(user):
        return Post.objects.filter(author=user).count()

    def __str__(self):
        return str(self.content[:20])

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default=False,max_length=10)

    def __str(self):
        return str(self.post)



class story(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE,related_name='story_post')
    image = models.ImageField( upload_to='story_pics')

    def __str__(self):
        return str(self.story_user, self.pk)
    
