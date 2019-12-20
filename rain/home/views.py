from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
# from forum.forms import PostForm
# from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login
# from accounts.models import UserProfile
from django.core.mail import send_mail

# Create your views here.
def view_home(request):
#    form = PostForm()
#     posts = Post.objects.order_by('date').reverse()
#     args = {'form':form,'posts':posts} 
    return render(request,'base.html')
    