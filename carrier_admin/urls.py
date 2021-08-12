from django.urls import path
from .views import *

urlpatterns = [
    path('',admin_home,name='dashboard-home'),
    path('create/post/',create_post,name='dashboard-post-create'),
    path('request/post/',request_post,name='dashboard-request-post')
]