from django.urls import path
from .views import *

urlpatterns = [
    path('register/',registrationView,name='auth-register'),
    path('activate/<str:uidb64>/<str:token>/',activate, name='activate'),
    path('login/',loginView,name='auth-login'),
    path('logout/',logoutView,name='auth-logout')

]