from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import ComplaintForm
from .models import Complaint
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login
from accounts.models import UserProfile
from django.core.mail import send_mail

def view_comp(request):
    form = ComplaintForm()
    posts = Complaint.objects.all().filter(user = request.user)#inlcude the filter
    args = {'form':form,'posts':posts}
    return render(request,'complaint/view.html',args)
    
@login_required
def raise_comp(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST,request.FILES)
        if form.is_valid():
            p = form.save(commit = False)
            p.status = True
            p.user = request.user
            p.save()
    else:
        form = ComplaintForm()
        args = {'form':form}
        return render(request,'complaint/create.html',args)
