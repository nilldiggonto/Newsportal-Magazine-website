from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from news_app.models import PostSubCategory,Post

# Create your views here.

@login_required(login_url='/auth/login/')
def admin_home(request):
    template_name = 'carrier/carrier_home.html'
    posts = Post.objects.filter(author=request.user)
    most_view = Post.objects.filter(author=request.user).order_by('-view_count')
    context = {
        'posts':posts,
        'most_view':most_view
    }
    return render(request,template_name,context)

@login_required(login_url='/auth/login/')
def create_post(request):
    category = PostSubCategory.objects.filter(active=True)

    template_name = 'carrier/create_post.html'
    context = {
        'category':category,
    }
    if request.method == "POST":

        title = request.POST.get('title')
 
        cats = request.POST.get('category')
        pic = request.FILES['pic']
        intro = request.POST.get('intro')

        description = request.POST.get('description')
        cat = PostSubCategory.objects.get(sub_name=cats)
        user = request.user

        Post.objects.create(author=user,scategory=cat,title=title,summary_one=description,intro_image=pic,intro=intro)
        return redirect('dashboard-home')

    return render(request,template_name,context=context)


def request_post(request):
    template_name = 'carrier/request_post.html'
    posts = Post.objects.filter(active=False)
    context = {
        'posts':posts,
    }
    return render(request,template_name,context=context)