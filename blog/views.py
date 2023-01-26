from django.shortcuts import render

# Create your views here.
#home page view
def Home(request):
    return render(request,'blog/home.html')