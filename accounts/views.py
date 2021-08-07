from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
# Create your views here.


def registrationView(request):
    user =User.objects.get(username="nill")
    template_name = 'accounts/register.html'

    
    return render(request,template_name)

def loginView(request):
    template_name = 'accounts/login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username,password)
        user = authenticate(username=username, password=password)
        # if user:

    return render(request,template_name)
    

