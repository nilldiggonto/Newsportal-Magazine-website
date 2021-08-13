from django.urls import path
from .views import *


urlpatterns = [
    path('',homepage,name='home-page'),
    path('api/latest/home/post/v1/',LatestPostListAPIView.as_view(),name='api-latest-home-v1'),
    path('category/<str:slug>/',category_page,name='category-page'),
    path('single/page/<str:slug>/',single_page,name='single-page'),

    
    path('api/latest/post/e1/<str:slug>/',CategoryPostListAPIView.as_view(),name='api-latest-post-e1'),
    
]