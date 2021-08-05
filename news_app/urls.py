from django.urls import path
from .views import *


urlpatterns = [
    path('',homepage,name='home-page'),
    path('category/<str:slug>/',category_page,name='category-page'),
    path('single/page/<str:slug>/',single_page,name='single-page'),

    
    path('api/latest/post/e1/<str:slug>/',LatestPostAPIView.as_view(),name='api-latest-post-e1'),
    
]