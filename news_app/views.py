from django.shortcuts import render
from .models import PostCategory,Post,PostSubCategory
from .serializers import PostSerializer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# from django.contrib.gis.utils import GeoIP
# from django.re
import requests
import json




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
    postcategory = PostCategory.objects.all()
    subcategory = PostSubCategory.objects.all()
    primary_featured = Post.objects.filter(primary_featured=True).order_by('-id')[0]
    featured_home = Post.objects.filter(featured=True)[:4]
    all_post = Post.objects.filter(active=True)[:5]
    popular_post = Post.objects.filter(active=True,popular=True)
    featured_category = PostSubCategory.objects.filter(featured=True)

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
        'prime_feature':primary_featured,
        'all_post':all_post,
        'popular_post':popular_post,
        'featured_category':featured_category,
        # 'country':country
    }
    return render(request,template_name,context)

########### CATEGORY PAGE
def category_page(request,slug):
    obj = get_object_or_404(PostSubCategory, slug=slug)
    postcategory = PostCategory.objects.all()
    template_name = 'pages/category.html'
    all_cat = PostSubCategory.objects.filter(category=obj.category)
    # print(all_cat)
    context = {
        "obj":obj,
        'postcategory':postcategory,
        'all_cat':all_cat
    }
    return render(request,template_name,context)

############## SINGLE PAGE
def single_page(request,slug):
    template_name = 'pages/single_page.html'

    postcategory = PostCategory.objects.all()
    obj = get_object_or_404(Post, slug=slug)
    # sub_category = PostSubCategory.objects.get()
    related_post = Post.objects.filter(slug=slug)


    # print(slug)
    context = {
       
        'postcategory':postcategory,
        'obj':obj
        
    }
    return render(request,template_name,context=context)


    


class LatestPostAPIView(APIView):
    # pagination_class = PostPagination
    pagination_class = CustomPagination()

    def get(self,request,format=None,slug=None):
        slug = self.kwargs.get('slug')
        # print(slug)
        scategory = PostSubCategory.objects.get(slug=slug)
        qs = Post.objects.filter(active=True,scategory=scategory)
        page = self.pagination_class.paginate_queryset(queryset=qs, request=request)
        if page is not None:
            serializer = PostSerializer(page, many=True)
            return self.pagination_class.get_paginated_response(serializer.data)
        serializer = PostSerializer(qs, many=True)

        return Response({'data':serializer.data})