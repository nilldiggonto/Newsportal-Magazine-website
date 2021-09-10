
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static


from django_otp.admin import OTPAdminSite
# admin.site.__class__ = OTPAdminSite

urlpatterns = [
    path('thenews/admin/carrier/', admin.site.urls),
    path('',include('news_app.urls')),
    path('auth/',include('accounts.urls')),
    path('dashboard/',include('carrier_admin.urls'))
    # path('accounts/', include('allauth.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'The NewsCarrier'
admin.site.site_title = 'The NewsCarrier'