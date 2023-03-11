from django.db import models
from django.db import models

class Applicant(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    dob = models.DateField()
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_number = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photos/')
    id_file_1 = models.FileField(upload_to='id_files/')
    id_file_2 = models.FileField(upload_to='id_files/')
    date_created = models.DateTimeField(auto_now_add=True)   
    
    def __str__(self):
        return self.name
