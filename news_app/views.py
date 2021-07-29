from django.shortcuts import render

# Create your views here.
def homepage(request):
    template_name = 'base/base.html'
    return render(request,template_name)