from django.shortcuts import render
from django.http import HttpResponseRedirect

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
    return render(request,'blog/signup.html')
#for login
def Login(request):
    return render(request,'blog/login.html')
#for logout
def Logout(request):
    return HttpResponseRedirect('/')
