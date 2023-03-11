from django.shortcuts import render,redirect
from django.contrib import messages
from . models import *


def applicant_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        father_name = request.POST.get('father-name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact-number')
        dob = request.POST.get('dob')
        emergency_contact_name = request.POST.get('emergency-contact-name')
        emergency_contact_number = request.POST.get('emergency-contact-number')
        photo = request.FILES.get('photo')
        id_file_1 = request.FILES.get('id-file-1')
        id_file_2 = request.FILES.get('id-file-2')
        if not name or not father_name or not email or not contact_number or not dob or not emergency_contact_name or not emergency_contact_number or not photo or not id_file_1 or not id_file_2:
            messages.error(request, 'All fields are required')
            return redirect('/')
        elif Applicant.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('/')
        else:
            form_data = Applicant(
                name=name,
                father_name=father_name,
                email=email,
                contact_number=contact_number,
                dob=dob,
                emergency_contact_name=emergency_contact_name,
                emergency_contact_number=emergency_contact_number,
                photo=photo,
                id_file_1=id_file_1,
                id_file_2=id_file_2
            )
            form_data.save()
            messages.success(request, 'Form submitted successfully')
            return redirect('/')
    return render(request,'form/applicant_form.html')