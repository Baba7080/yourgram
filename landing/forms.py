from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from time import time
import datetime
from datetime import time
from django.contrib.auth.models import User
from django.db.models import fields
from django.shortcuts import render
from .models import *
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Post
from social.models import Comment,stori
from django.http import HttpResponseRedirect

#Login Form



class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':"form-control"}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':"form-control"}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':"form-control"}))
    date_of_join = forms.DateField(initial=datetime.date.today)
    # time_join = forms.DateTimeField(initial=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    time_of_join = forms.TimeField(initial=datetime.datetime.now)
    #  forms.DateTimeField(initial = datetime.datetime.now)
    # Category = forms.ChoiceField(choices = Catogories)
    class Meta:
        model = User
        fields = ['username','date_of_join','time_of_join','email','password1','password2']
        label = {'email':'Email'}
        widget = {'username':forms.TextInput(attrs={'class':'form-control'})}


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...'
            }))

    class Meta:
        model = Comment
        fields = ['comment']



class ProfileUpdateForm(forms.ModelForm):
    # Category = forms.CharField(max_length=100)
    # bio = forms.CharField(max_length=100)
    # image = forms.ImageField()
    class Meta:

        model = Profile
        fields = ['image']
class Newpost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','image','content']
#Login Form
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs=
        {'autocomplete':'current-password', 'class':'form-control'}))


#Change Password Form
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=('Old Password'),strip=False, widget=forms.PasswordInput
        (attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))

    new_password1 = forms.CharField(label=('New Password'),strip=False, widget=forms.PasswordInput
        (attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.
        password_validators_help_text_html())

    new_password2 = forms.CharField(label=('Confirm New Password'),strip=False, widget=forms.PasswordInput
        (attrs={'autocomplete':'new-password','class':'form-control'}))


# Reset Password Form
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=('Email'),max_length=255, widget=forms.EmailInput
        (attrs={'autocomplete':'email','class':'form-control'}))



#Confirm Reset Password Form
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=('New Password'),strip=False, widget=forms.PasswordInput
        (attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.
        password_validators_help_text_html())
    new_password2 = forms.CharField(label=('Confirm New Password'),strip=False, widget=forms.PasswordInput
        (attrs={'autocomplete':'new-password','class':'form-control'}))




class UserUpdateForms(forms.ModelForm):
    class Meta:
        model = User
        fields = []


class story_update(forms.ModelForm):
    class Meta:
        model = stori
        fields = ['image']


# class Categoryselection(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['Category']