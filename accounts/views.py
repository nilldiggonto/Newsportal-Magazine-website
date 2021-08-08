from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.


def registrationView(request):
    user =User.objects.get(username="nill")
    template_name = 'accounts/register.html'

    
    return render(request,template_name)

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
   
    

