from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


from .models import Contacts
# Create your views here.
def index(request):
    return render(request,'index.html',{'titleName':"home"})

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        msg = request.POST.get("msg")
        c= Contacts(name=name,emailid=email,phone=phone,msg=msg)
        c.save()
    return render(request,'contact.html')

def product(request,name):
    print("hello ",name)
    return render(request,'product.html',{'name':name})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username="username", password="password")
        if user is not None:
            login(request,user)
        # A backend authenticated the credentials
            return redirect('/home')
        else:
        # No backend authenticated the credentials
            return redirect('/login',{'msg':"wrong username or password !!!"})
    return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
        
        if password == cpassword:
            user = User.objects.create_user( username ,email,password)
            user.save()
            return redirect('/login')
        
    return render(request,'signup.html')

def logout_view(request):
    logout(request)
    return redirect('/login')
    
