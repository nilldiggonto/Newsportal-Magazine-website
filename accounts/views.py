from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.


def registrationView(request):
    user =User.objects.get(username="nill")
    template_name = 'accounts/register.html'

    if request.method == 'POST':
        username = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():

            return render(request,template_name,{'valid':False})
        else:
            user = User.objects.create(first_name=fname,last_name=lname,username=username,email=username,is_active=False)
            user.set_password(password)
            # user.active=False
            user.save()
            return redirect('auth-login')
    
    return render(request,template_name,{'valid':True})

def loginView(request):
    template_name = 'accounts/login.html'
    if request.user.is_authenticated:
        return redirect('dashboard-home')
        
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username,password)
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('dashboard-home')
        else:
            pass

    return render(request,template_name)

@login_required
def logoutView(request):
    user = logout(request)
    return redirect('home-page')
   
    

