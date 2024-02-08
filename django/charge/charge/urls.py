from django.contrib import admin
from django.urls import path, include
from charge_api import urls as charge_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('charge/', include(charge_urls))
]
