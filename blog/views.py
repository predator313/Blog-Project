from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignupForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
#home page view
def Home(request):
    return render(request,'blog/home.html')

#about view
def About(request):
    return render(request,'blog/about.html')
#contact page
def Contact(request):
    return render(request,'blog/contact.html')

#for dashboard
def Dashboard(request):
    return render(request,'blog/dashboard.html')

#for signup
def Signup(request):
    if request.method=="POST":
        fm=SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'congratulations you now become auther')
            fm.save()
    else:
       fm=SignupForm()
    return render(request,'blog/signup.html',{'form':fm})
#for login
def Login(request):
    # if not request.user.is_authenticated:
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user:
                    login(user,request)
                    messages.success(request,'successfully logged in !!!')
                    return HttpResponseRedirect('/dash/')
        else:
            fm=LoginForm()
        return render(request,'blog/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dash/')
#for logout
def Logout(request):
    return HttpResponseRedirect('/')
