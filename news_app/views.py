from django.shortcuts import render
from .models import PostCategory,Post,PostSubCategory

# Create your views here.
def homepage(request):
    template_name = 'base/base.html'
    postcategory = PostCategory.objects.all()
    subcategory = PostSubCategory.objects.all()
    primary_featured = Post.objects.filter(primary_featured=True).order_by('-id')[0]
    featured_home = Post.objects.filter(featured=True)[:4]

    context = {
        'postcategory':postcategory,
        'featured':featured_home,
        'subcategory':subcategory,
        'prime_feature':primary_featured
    }
    return render(request,template_name,context)