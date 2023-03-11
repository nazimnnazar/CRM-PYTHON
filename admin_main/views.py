from django.shortcuts import render
from core.models import*


def admin_main(request):
    st = student.objects.all()
    return render(request,'admin_mainn.html',{'st':st})

def errorpage(request):
    return render(request, 'pages-error-404.html')