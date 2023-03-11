from django.shortcuts import render,redirect
from . models import*
def version2(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        father_name = request.POST.get('father_name')
        contact_number = request.POST.get('contact_number')
        date_of_birth = request.POST.get('date_of_birth')
        email = request.POST.get('email')
        emergency_contact_person = request.POST.get('emergency_contact_person')
        emergency_contact_number = request.POST.get('emergency_contact_number')
        profile_image = request.FILES.get('profile_image')
        id_card_file_upload_1 = request.FILES.get('id_card_file_upload_1')
        id_card_file_upload_2 = request.FILES.get('id_card_file_upload_2')
        
        errors = {}
        if not name:
            errors['name'] = 'Name is required.'
        if not father_name:
            errors['father_name'] = 'Father name is required.'
        if not contact_number:
            errors['contact_number'] = 'Contact number is required.'
        if not date_of_birth:
            errors['date_of_birth'] = 'Date of birth is required.'
        if not email:
            errors['email'] = 'Email is required.'
        if not emergency_contact_person:
            errors['emergency_contact_person'] = 'Emergency contact person is required.'
        if not emergency_contact_number:
            errors['emergency_contact_number'] = 'Emergency contact number is required.'
        if not profile_image:
            errors['profile_image'] = 'Profile image is required.'
        if not id_card_file_upload_1:
            errors['id_card_file_upload_1'] = 'ID card file 1 is required.'
        if not id_card_file_upload_2:
            errors['id_card_file_upload_2'] = 'ID card file 2 is required.'
        if errors:
            return render(request, 'version2/version2_form.html', {'errors': errors})
        
        person = Person(
            name=name,
            father_name=father_name,
            contact_number=contact_number,
            date_of_birth=date_of_birth,
            email=email,
            emergency_contact_person=emergency_contact_person,
            emergency_contact_number=emergency_contact_number,
            profile_image=profile_image,
            id_card_file_upload_1=id_card_file_upload_1,
            id_card_file_upload_2=id_card_file_upload_2,
        )
        person.save() 

        return redirect('/')
    else:
        return render(request,'version2/version2_form.html')