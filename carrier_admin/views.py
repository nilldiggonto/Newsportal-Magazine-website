from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def admin_home(request):
    template_name = 'carrier/carrier_home.html'
    return render(request,template_name,{})
