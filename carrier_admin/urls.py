from django.urls import path
from .views import *

urlpatterns = [
    path('',admin_home,name='dashboard-home'),
]