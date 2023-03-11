from django.db import models

class Applicant(models.Model):
    name = models .CharField(max_length=200)
    father_name =models.CharField(max_length=200)
    contact_number = models.CharField(max_length=2000)
    date_of_birth = models.DateField()
    email =models.EmailField()
    emergency_contact_person = models.CharField(max_length=200)
    emergency_contact_number = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='applicant_image/')
    id_card_file_upload_1 = models.FileField(upload_to='id_card_files/')
    id_card_file_upload_2 = models.FileField(upload_to='id_card_files/')

    def __str__(self):
        return self.name