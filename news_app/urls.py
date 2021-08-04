from django.urls import path
from .views import *


urlpatterns = [
    path('',homepage,name='home-page'),
    path('category/<str:slug>/',category_page,name='category-page'),

    
    path('api/latest/post/e1/',LatestPostAPIView.as_view(),name='api-latest-post-e1'),
    
]