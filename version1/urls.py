from django.urls import path
from . import views
urlpatterns = [
    path('applicant_form/',views.applicant_form,name='applicant_form')
]