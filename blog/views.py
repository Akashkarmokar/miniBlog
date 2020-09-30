from django.shortcuts import render,HttpResponseRedirect

# Create your views here.

#home
def home(request):
    return render(request,'blog/home.html')

#about
def about(request):
    return render(request,'blog/about.html')

#contact
def contact(request):
    return render(request,'blog/contact.html')

#Dashboard
def dashboard(request):
    return render(request,'blog/dashboard.html')

#Logout
def user_logout(request):
    return HttpResponseRedirect('/')

#Login
def user_login(request):
    return render(request,'blog/login.html')

#signup
def signup(request):
    return render(request,'blog/signup.html')