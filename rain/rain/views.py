from django.shortcuts import redirect
from django.shortcuts import render,HttpResponse,redirect 

def login_redirect(request):
    # return redirect('/<path name redirected after login>')
    return 0 #dummy return

def about(request):
    return render(request,'accounts/about.html')