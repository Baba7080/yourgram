from django.shortcuts import render,get_list_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import CustomerRegistrationForm,ProfileUpdateForm,UserUpdateForms,Newpost,CommentForm,story_update
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Profile,Post,Like,story
from django.views import generic,View
from django.contrib.auth.models import User
from django.views.generic import DetailView,CreateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from social.models import Comment,stori
from django.http import Http404
from django.views.generic import View
from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout


def update_story(request):
    if request.method == 'POST':
        form = story_update(request.POST,request.FILES)
        if form.is_valid():
            user = request.user
            register_user = user.id
            register_profile = Profile.objects.get(user =register_user)
            print('profile',register_profile)
            form.instance.user=user
            form.instance.story_user = register_profile
            form.save()
            return redirect('update_story')
            # form.save()
    else:
        form = story_update()
    context= {
        'form':form

    }
    return render(request,'story_update.html',context)

def view_story(request,pk):
    author  =  request.user
    story_detail = stori.objects.filter(pk = pk)

    for i in story_detail:
        a = i.story_user
    if a == author:
        user=request.user.id
        b = True
        if request.method == 'POST':
            story_detail.delete()
            return HttpResponseRedirect('/')
    else:
        messages.success(request,"You can't delete or make any change to other's post please try it with you own post")
        return render(request,'story_detail.html',{'story_detail':story_detail,})

    return render(request,'story_detail.html',{'story_detail':story_detail, 'b':b})
@login_required
def delete_post(request,pk):
    post_detail = Post.objects.filter(pk = pk)
    user=request.user.id
    if request.method == 'POST':
        
        post_detail.delete()
        return HttpResponseRedirect('/')
    return render(request,'profilee.html')

def PostList(request):
    if request.user.is_authenticated:
        status = stori.objects.all()
        
        prof = Profile.objects.all()
        prof = prof[:2]
        # print(c,"poo")
        queryset = Post.objects.order_by('-created_on')
        user= request.user
        return render(request,'home.html',{'queryset':queryset,'prof':prof,'user':user,'status':status})
    else:
        return redirect('login')


def PostComment(request):
    user = request.user
    if request.method == 'POST':
        c_form = CommentForm(request.post)
        if c_form.is_valid():
            # user = user
            post = request.POST.get(id)
            c_form.save()
        else:
            c_form.save()
        return render(request, 'home.html')
    else:
        c_form = CommentForm()
    return render(request, 'post_detail', {'c_form':c_form})
@login_required
def update_post(request,pk):
    user = request.user
    update_postt = Post.objects.get(id = pk)
    postii = Post.objects.filter(id =pk)
    for k in postii:
        a = k.author
        print(a,"aaa",user)
    if user == a:
        productss= Newpost(instance=update_postt)
        if request.method == 'POST':
            productss= Newpost(request.POST,request.FILES,instance=update_postt)
            if productss.is_valid():
                user = request.user
                author_id = request.user.id
                productss.instance.user=user
                productss.instance.author = user
                productss.save()
                return redirect('newpost')
        else:
            productss= Newpost()
        context={
                'product':productss,
                'postii':postii
            }
        return render(request, 'update_post.html',context)
    else:
        return HttpResponse('Your credential is not valid to Update  other post....You are going to blocked and we will take a strict action agains you')


def perform_on_post(request,pk):
    author = request.user
    user_post_detail_by_his_profile = Post.objects.get(id = pk)
    postii = Post.objects.filter(id =pk)
    # ddd = Post.objects.get(author=)
    for k in postii:
        a = k.author
        print(a,"aaa",author)
    # print(postii,"author")
    post_detail = Post.objects.filter(pk = pk)
    user=request.user.id
    if user == a:
        if request.method == 'POST':
            
            post_detail.delete()
            return HttpResponseRedirect('/')
        return render(request,'user_post_detail_by_his_profile.html',{'postii':postii})
    else:
        return HttpResponse('Your credential is not valid to perform other post....You are going to blocked and we will take a strict action agains you')


def PostDetail(request,id):
    obj = get_list_or_404(Post,pk=id)
    pst = Post.objects.get(id = id)
    postt = Comment.objects.filter(post= pst)
    pro = Profile.objects.all()
    print(pro,"pro")
    print("upppr profile h ")
    user = request.user
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            user = request.user
            # post = request.POST.get(id)
            c_form.instance.auther = user
            c_form.instance.post = pst
            c_form.save()
        else:
            c_form.save()
        return redirect('/')
    else:
        c_form = CommentForm()
    
    # return render(request, 'post_detail', {'c_form':c_form})
    return render(request, 'post_detail.html',{'obj':obj, 'postt':postt, 'pro':pro,'c_form':c_form})


def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj =Post.objects.get(id = post_id)
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        like, created = Like.objects.get_or_create(user=user, post_id=post_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
    return redirect('home')

# def profiled(request):
#     detaill =  Profile.objects.all()
#     return render(request, 'prof_detail.html',{'detaill':detaill})


class profiled(DetailView):
    model = Profile
    template_name = 'prof_detail.html'
    def get_context_data(self, **kwargs):
        context = super(profiled, self).get_context_data(**kwargs)
        pk = self.kwargs.get('id')
        context['post'] = Post
        print(post,"post")
        return context
  

def all_user(request):
    prof = Profile.objects.all()
    return render(request, 'all_user.html',{'prof':prof})

def CustomerRegistrationView(request):
    profile_id = request.session.get('ref_profile')
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            if profile_id is not None:
                recommended_by_profile = Profile.objects.get(id=profile_id)
                print('profile',recommended_by_profile)
                instance = form.save()
                register_user = User.objects.get(id=instance.id)
                register_profile = Profile.objects.get(user =register_user)
                register_profile.recommended_by = recommended_by_profile.user
                register_profile.save()
            else:
                form.save()
            user = form.save(commit=False)
            user.is_active = False
            print("1 active = flse")
            user.save()
            
         
            return render(request , 'login.html')

    else:
        form = CustomerRegistrationForm()
    print("yyyyy")
    return render(request, 'customerregistration.html', {'form': form})


def postt(request):
    if request.method == 'POST':
        productss= Newpost(request.POST,request.FILES)
        if productss.is_valid():
            user = request.user
            author_id = request.user.id
            productss.instance.user=user
            productss.instance.author = user
            productss.save()
            return redirect('newpost')
    else:
        productss= Newpost()
    context={
            'product':productss
        }
    return render(request, 'post.html',context)


def post(request):
    if request.method == "POST":
        form = Newpost(request.POST, request.FILES)
        # profile = Profile.objects.get(user=request.user)

    # if 'submit_p_form' in request.POST:
        print(request.POST)
        # p_form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            print('start')
            form.save()
            print('save')
            messages.success(request,f'You had created a new post succesfully')
            print("valid")
            return redirect('profilev')

    else:
        form = Newpost(request.POST,instance=request.user)

    return render(request, 'post.html',{"form":form})

def logout(request):
    return render(request, 'logout.html')

def Profile_pic_update(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request,f'Your Account Has Been Updated')
            return redirect('profilev')
    else:
        p_form = ProfileUpdateForm(request.POST,instance=request.user)

    return render(request, 'profile_pic_updation.html',{"p_form":p_form})

@login_required
def profilev(request):
    num_post = Post.objects.filter(author=request.user).count()
    total_image = Post.objects.filter(image=request.user)
    # Fetch the user post  pst
    pst = Post.objects.filter(author=request.user)
    print("num",num_post)
    print(total_image,"total_image")
    print(pst,'psst')
    # return render(request, 'some_template.html', {'num_post': num_post})
    # add = Customer.objects.filter(user=request.user)
    return render(request, 'profilee.html',{'num_post': num_post,'pst':pst})
    # {'add':add, 'active':'btn-primary'}

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/index.html')
