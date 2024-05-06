from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def signout(request):
    logout(request)
    return redirect('home')
def show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True

        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            #create user account
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            #create customer account
            Customer.objects.create(
                name=username,
                user=user,
                phone=phone,
                address=address
            )
            success_message="user registred successfully"
            messages.success(request,success_message)
            context
        except Exception as e:
            error_message='username is already exist or invalid inputs'
            messages.error(request,error_message)

    
    if request.POST and 'login' in request.POST:
        context['register']=False
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid user credintials')
           



    return render (request,'account.html',context)

