from django.shortcuts import render

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

#for signup
def Signup(request):
    pass
#for login
def Login(request):
    pass
#for logout
def Logout(request):
    pass
