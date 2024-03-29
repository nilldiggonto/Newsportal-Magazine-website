from django.shortcuts import render
from .models import *
from .serializers import PostSerializer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# from django.contrib.gis.utils import GeoIP
# from django.re
import requests
import json



from django.db.models import Q
############# DRF IMPORT
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions,pagination
from django.contrib.auth.models import User


## For pagination

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        print ("returning FORWARDED_FOR")
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        print ("returning REAL_IP")
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        print ("returning REMOTE_ADDR")
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_country(ip):
    ip_address = ip

    # URL to send the request to
    request_url = 'https://geolocation-db.com/jsonp/' + ip_address
    # Send request and decode the result
    response = requests.get(request_url)
    result = response.content.decode()
    # Clean the returned string so it just contains the dictionary data for the IP address
    result = result.split("(")[1].strip(")")
    # Convert this data into a dictionary
    result  = json.loads(result)
    country = result['country_name']
    return country


##===========================================

class CustomPagination(pagination.PageNumberPagination):
    page_size = 1  
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })

# Create your views here.
def homepage(request):
    template_name = 'base/base_home.html'
    bangla = request.GET.get('lang')
    # print(bangla)
    lang = 'english'
    if bangla == 'bangla':
        postcategory = PostCategory.objects.filter(bangla=True)
        subcategory = PostSubCategory.objects.filter(bangla=True)
        # primary_featured = Post.objects.filter(primary_featured=True,active=True,bangla=True).order_by('-id')[0]
        featured_home = Post.objects.filter(featured=True,active=True,bangla=True)
        all_post = Post.objects.filter(active=True,bangla=True)
        popular_post = Post.objects.filter(active=True,popular=True,bangla=True)
        featured_category = PostSubCategory.objects.filter(featured=True,bangla=True)
        lang = 'bangla'
    else:
        postcategory = PostCategory.objects.filter(bangla=False)
        subcategory = PostSubCategory.objects.filter(bangla=False)
        # primary_featured = Post.objects.filter(primary_featured=True,active=True,bangla=True).order_by('-id')[0]
        featured_home = Post.objects.filter(featured=True,active=True,bangla=False)
        all_post = Post.objects.filter(active=True,bangla=False)
        popular_post = Post.objects.filter(active=True,popular=True,bangla=False)
        featured_category = PostSubCategory.objects.filter(featured=True,bangla=False)


    # print( request.META['REMOTE_ADDR'])
    # ip = get_client_ip(request)
    # country = get_country(ip)
    # if country == 'Not found':
    #     country = 'Bangladesh'
    # print(a)
    # IP address to test



    context = {
        'postcategory':postcategory,
        'featured':featured_home,
        'subcategory':subcategory,
        # 'prime_feature':primary_featured,
        'all_post':all_post,
        'popular_post':popular_post,
        'featured_category':featured_category,
        'lang':lang
        # 'country':country
    }
    return render(request,template_name,context)

########### CATEGORY PAGE
def category_page(request,slug):
    lang= 'english'
    obj = get_object_or_404(PostSubCategory, slug=slug)
    postcategory = PostCategory.objects.filter(bangla=False)
    template_name = 'pages/category.html'
    all_cat = PostSubCategory.objects.filter(category=obj.category,bangla=False)
    # print(all_cat)
    if obj.bangla:
        lang = 'bangla'
        postcategory = PostCategory.objects.filter(bangla=True)

        all_cat = PostSubCategory.objects.filter(category=obj.category,bangla=True)

    context = {
        "obj":obj,
        'postcategory':postcategory,
        'all_cat':all_cat,
        'lang':lang
    }
    return render(request,template_name,context)

############## SINGLE PAGE
def single_page(request,slug):
    template_name = 'pages/single_page.html'
    lang= 'english'

    postcategory = PostCategory.objects.filter(bangla=False)
    obj = get_object_or_404(Post, slug=slug)
    related_post = Post.objects.filter(slug=slug)

    if obj.bangla:
        lang = 'bangla'
        postcategory = PostCategory.objects.filter(bangla=True)

        # all_cat = PostSubCategory.objects.filter(category=obj.category,bangla=True)

    # if obj:
    if obj:
        obj.view_count = int(obj.view_count) + 1
        obj.save()
    # sub_category = PostSubCategory.objects.get()

    all_cat = PostSubCategory.objects.filter(category=obj.scategory.category)

    comment_count = obj.comment.all().count()
    # print(comment_count)
    # print(slug)
    context = {
       
        'postcategory':postcategory,
        'obj':obj,
        'all_cat':all_cat,
        'lang':lang,
        'comment_count':comment_count,
        
    }
    return render(request,template_name,context=context)


    


class CategoryPostListAPIView(APIView):
    # pagination_class = PostPagination
    pagination_class = CustomPagination()

    def get(self,request,format=None,slug=None):
        slug = self.kwargs.get('slug')
        # print()
        bangla = request.GET.get('lang')
        if bangla == 'bangla':
            scategory = PostSubCategory.objects.get(slug=slug,bangla=True)
            qs = Post.objects.filter(active=True,scategory=scategory,bangla=True)
            page = self.pagination_class.paginate_queryset(queryset=qs, request=request)
            if page is not None:
                serializer = PostSerializer(page, many=True)
                return self.pagination_class.get_paginated_response(serializer.data)
            serializer = PostSerializer(qs, many=True)
        else:
            scategory = PostSubCategory.objects.get(slug=slug,bangla=False)
            qs = Post.objects.filter(active=True,scategory=scategory,bangla=False)
            page = self.pagination_class.paginate_queryset(queryset=qs, request=request)
            if page is not None:
                serializer = PostSerializer(page, many=True)
                return self.pagination_class.get_paginated_response(serializer.data)
            serializer = PostSerializer(qs, many=True)


        return Response({'data':serializer.data})

class LatestPostListAPIView(APIView):
    pagination_class = CustomPagination()

    def get(self,request,format=None):
        bangla = request.GET.get('lang')
        if bangla == 'bangla':

            qs = Post.objects.filter(active=True,bangla=True)
            page = self.pagination_class.paginate_queryset(queryset=qs, request=request)
            if page is not None:
                serializer = PostSerializer(page, many=True)
                return self.pagination_class.get_paginated_response(serializer.data)
            serializer = PostSerializer(qs, many=True)
        else:
            qs = Post.objects.filter(active=True,bangla=False)
            page = self.pagination_class.paginate_queryset(queryset=qs, request=request)
            if page is not None:
                serializer = PostSerializer(page, many=True)
                return self.pagination_class.get_paginated_response(serializer.data)
            serializer = PostSerializer(qs, many=True)

        return Response({'data':serializer.data})



class CommentAPIView(APIView):
    def post(self,request):
  
        slug = request.data['slug']
        name = request.data['name']
        comment = request.data['comment']
        
        post = Post.objects.get(slug=slug)
        Comment.objects.create(post=post,name=name,oponion=comment,comment_to=post.author)
        # print(slug,name,comment)
        return Response({'status':'thnks'})


###############################
def searchView(request):
    template_name = 'pages/search.html'
    if request.method == 'GET':
        search = request.GET.get('fsearch')
        # print(search)
        qs = ''
        if search:
            qs = Post.objects.filter(Q(title__icontains=search) | Q(intro__icontains=search) | Q(summary_one__icontains=search))
        context = {
            'search':search,
            'qs':qs
        }
        
        return render(request,template_name,context)