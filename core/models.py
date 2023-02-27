from django.db import models



class student(models.Model):
    student_name = models.CharField(max_length=255)
    police_verification = models.BooleanField(default=False)
    id_idcard = models.CharField(max_length=255, blank=True)
    student_image = models.ImageField(upload_to='student_images/', blank=True)
    email = models.EmailField(unique=True)
    relastion_with_contact_person = models.CharField(max_length=255, blank=True)
    alternative_contact_number = models.CharField(max_length=20, blank=True)
    contact_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    date_of_birth = models.DateField(null=False)
    student_father_name = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.student_name