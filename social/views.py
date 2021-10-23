from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post, Comment
from .forms import CommentForm
# Create your views here.
# class PostListView(LoginRequiredMixin, View):
#     def get(self, request, *args, **kwargs):
#         posts = Post.objects.all().order_by('-created_on')
#         form = PostForm()

#         context = {
#             'post_list': posts,
#             'form': form,
#         }
#         return render(request, 'social/post_list.html', context)