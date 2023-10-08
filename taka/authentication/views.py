from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required(login_url='register') 
@csrf_exempt
def home_page(request):
    user = request.user

    context = {
            'user': user,

        }
    return render(request, 'homepage/index.html', context)

def registration(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        mail=request.POST.get('email')
        pass1=request.POST.get('password')
        myuser=User.objects.create_user(uname,mail,pass1)
        myuser.save()
        return redirect('login')


    return render(request,'authentication/home.html')


def LoginView(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request, username=username,password=pass1)
        if user is not None:
            login(request,user)
            request.session['user']=username
            return redirect('home')


        
    return render(request,'authentication/home.html')
        
def logoutView(request):
    logout(request)
    request.session.clear()

    return redirect('login')



    



