from django.shortcuts import render,redirect
from . models import*
from .forms import*
# Create your views here.

def entrypage(request):
    return render(request, 'core/entrypage.html')

def nopermit(request):
    return render(request, 'no_permit/nopermit.html')

def forms(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('payment')
    else:
        form = StudentForm()
    return render(request,'core/form.html',{'form':form})

def payment(request):
    return render(request,'core/payment/payment.html')

def form_new(request):
    return render(request,'forms-elements.html')

def register_form(request):
    return render(request,'tailwind_register/ register_form.html')

def navform(request):
    return render(request, 'tailwind_register/navform_new.html')