from django.shortcuts import render
from .models import PostCategory

# Create your views here.
def homepage(request):
    template_name = 'base/base.html'
    postcategory = PostCategory.objects.all()

    context = {
        'postcategory':postcategory,
    }
    return render(request,template_name,context)