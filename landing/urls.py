from django import views
from django.contrib import admin
from django.urls import path
from .forms import LoginForm
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from . import views
from .views import *
urlpatterns = [
    path('',PostList,name='home'),
    # path('<slug:slug>/',PostDetail.as_view(), name='post_detail'),
    path('profiled/<int:pk>',profiled.as_view(),name='profiled'),
    # path('newpost/',postt.as_view(),name='newpost'),
    # Post 
    path('newpost/',postt,name="newpost"),
    # Update Post
    path('update_post/<int:pk>/update',update_post,name='update_post'),
    # Delete the post
    path('delete_post/<int:pk>/remove',delete_post,name='delete_post'),
    # post detail toEit delete update by user
    path('peform_on_post/<int:pk>',perform_on_post,name="perform_on_post"),

# Post Comment on a Post
    path('Comment/',PostComment,name='Comment'),
    path('like/',like_post,name='like-post'),
    # all profile
    path('see_all',all_user,name="see_all"),
    # story updation  
    path('story/',update_story,name="update_story"),
    # story_view
    path('view_story/<int:pk>', view_story,name='view_story'),
    # Profile Updation

    path('profile_pic_update',Profile_pic_update,name='profile_pic_update'),
    # path('',views.PostList,name='home'),
    path('customerregistration',CustomerRegistrationView,name='registration'),
    path('accounts/profile/',profilev,name='profilev'),
    
    path('login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
    # path('login/',LoginView.as_view(),name='login'),

    # 3-Logout
    path('logout/', auth_views.LogoutView.as_view(next_page='logoutt'),name='logout'),
    path('logoutt/',logout,name='logoutt'),
    path('<int:id>/',PostDetail, name='post_detail'),
    

    # 4-password change


]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)





# from django.urls import path
# from landing.views import Index

# urlpatterns = [
#     path('', Index.as_view(), name='index'),
# ]
