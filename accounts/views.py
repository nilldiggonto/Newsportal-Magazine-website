from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.


def registrationView(request):
    user =User.objects.get(username="nill")
    template_name = 'accounts/register.html'

    
    return render(request,template_name)
