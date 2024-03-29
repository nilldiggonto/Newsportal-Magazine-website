from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from news_app.models import PostSubCategory,Post,Comment

# Create your views here.

@login_required(login_url='/auth/login/')
def admin_home(request):
    template_name = 'carrier/carrier_home.html'
    posts = Post.objects.filter(author=request.user)
    pending_posts = Post.objects.filter(author=request.user,active=False)
    most_view = Post.objects.filter(author=request.user).order_by('-view_count')
    comments = Comment.objects.filter(comment_to=request.user)
    context = {
        'posts':posts,
        'most_view':most_view,
        'comments':comments,
        'pending_posts':pending_posts
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

@staff_member_required
def request_post(request):
    template_name = 'carrier/request_post.html'
    posts = Post.objects.filter(active=False)
    context = {
        'posts':posts,
    }
    return render(request,template_name,context=context)

@staff_member_required
def approved_post(request,slug):
    post = Post.objects.get(slug=slug)
    post.active= True
    post.save()
    return redirect('dashboard-request-post')