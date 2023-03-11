from django.urls import path
from . import views

urlpatterns = [
    path('version2/',views.version2,name='version2'),
]