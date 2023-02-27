from django.urls import path
from . import views

urlpatterns = [
    path('admin_main',views.admin_main,name='admin_main'),
    path('errorpage/',views.errorpage,name='errorpage'),
]