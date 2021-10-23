from django.contrib import admin

# Register your models here.
from .models import Post,Profile,Like,story

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Like)
admin.site.register(story)