from django.urls import path
from . import views

urlpatterns = [
    path('',views.entrypage,name='entrypage'),
    path('nopermit/',views.nopermit,name='nopermit'),
    path('forms/',views.forms,name='forms'),
    path('payment',views.payment,name='payment'),
    path('form_new/',views.form_new,name='form_new'),
    path('register_form/',views.register_form,name='register_form'),
    path('navform/',views.navform,name='navform'),
]