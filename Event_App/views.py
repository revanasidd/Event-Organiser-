from json import load
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required


def home(request):
    family=Family.objects.all()
    bussiness = Bussiness.objects.all()
    cluture = Culture.objects.all()
    charity = Charity.objects.all()
    return render(request,'base.html',{'family':family,'bussiness':bussiness,'cluture':cluture,'charity':charity})

# Create your views here.

def Register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'you Restration Successfuly created')
            return redirect('/')
    form = RegisterForm()
    return render(request,'register.html',{'form':form}) 


# def Register(request):
#     if request.method=='POST':
#         first_name=request.POST['first_name']
#         last_name=request.POST['first_name']
#         username=request.POST['username']
#         email=request.POST['email']
#         password1=request.POST['password1']
#         password2=request.POST['password2']

#         if password1==password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, 'Username taken')
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email Alreday exist')
#                 return redirect('register')
#             else:
#                 user=User.objects.create_user(first_name=first_name, last_name=last_name,username=username,email=email,password=password1)
                
#                 user.save()
#                 messages.info(request,'Your account has been created')
#             return redirect('login')

#         else:
#             messages.info(request, 'Password did not match')
#     return render(request, 'register.html')

def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'Login Successfull')
            return redirect('/')
    messages.warning(request,'Invalid credentials')
    return render(request,'login.html')

def Logout(request):
    auth.logout(request)
    messages.info(request,"Logeed Out Successfull")
    return redirect('/')

@login_required
def booked_events(request):
    data = Bookevent.objects.all()
    return render(request,'events.html',{'data':data})

def book_event(request):
    if request.method=='POST':
        form = BookEventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'your event is booked succfuly')
            return render(request,'booking_event.html')
    else:
        form = BookEventForm()
        return render(request,'event/booking_event.html',{'form':form})

def Family_event(request):
    data = Family.objects.all()
    return render(request,'event/family_event.html',{'data':data})
def Cluture_event(request):
    data = Culture.objects.all()
    return render(request,'event/cluture_event.html',{'data':data})
def Charity_event(request):
    data = Charity.objects.all()
    return render(request,'event/charity_event.html',{'data':data})
def Bussiness_event(request):
    data = Bussiness.objects.all()
    return render(request,'event/bussiness_event.html',{'data':data})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Thank You for contact us')
            return redirect('/')
    else:
        form = ContactForm()
        return render(request,'event/contact_us.html', {'form':form})