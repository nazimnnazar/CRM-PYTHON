from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('admin_main/',include('admin_main.urls')),
    path('version1/',include('version1.urls')),
    path('version2/',include('version2.urls')),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)