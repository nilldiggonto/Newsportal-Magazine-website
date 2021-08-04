from django.shortcuts import render
from .models import PostCategory,Post,PostSubCategory
from .serializers import PostSerializer
# from django.re


############# DRF IMPORT
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions,pagination
from django.contrib.auth.models import User


## For pagination
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
    template_name = 'base/base.html'
    postcategory = PostCategory.objects.all()
    subcategory = PostSubCategory.objects.all()
    primary_featured = Post.objects.filter(primary_featured=True).order_by('-id')[0]
    featured_home = Post.objects.filter(featured=True)[:4]
    all_post = Post.objects.filter(active=True)[:5]
    popular_post = Post.objects.filter(active=True,popular=True)
    featured_category = PostSubCategory.objects.filter(featured=True)

    context = {
        'postcategory':postcategory,
        'featured':featured_home,
        'subcategory':subcategory,
        'prime_feature':primary_featured,
        'all_post':all_post,
        'popular_post':popular_post,
        'featured_category':featured_category
    }
    return render(request,template_name,context)

########### CATEGORY PAGE
def categoryPage(request,slug):
    pass


class LatestPostAPIView(APIView):
    # pagination_class = PostPagination
    pagination_class = CustomPagination()

    def get(self,request,format=None):
        qs = Post.objects.filter(active=True)
        page = self.pagination_class.paginate_queryset(queryset=qs, request=request)
        if page is not None:
            serializer = PostSerializer(page, many=True)
            return self.pagination_class.get_paginated_response(serializer.data)
        serializer = PostSerializer(qs, many=True)

        return Response({'data':serializer.data})