from django import forms
from .models import*

class StudentForm(forms.ModelForm):
    student_name = forms.CharField(max_length=500,widget=forms.TextInput(attrs={
        "class":"form-control", "placeholder":"Name"
    }))
    police_verification = forms.BooleanField(widget=forms.TextInput(attrs={
        "class":"form-control ", "placeholder":" Police verification"
    }))
    id_idcard = forms.CharField(max_length=500,widget=forms.TextInput(attrs={
        "class":"form-control", "placeholder":" ID"
    }))
    student_image = forms.ImageField(widget=forms.FileInput(attrs={
        "class":"form-control", "placeholder":" "
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "class":"form-control", "placeholder":" Email"
    }))
    relastion_with_contact_person = forms.CharField(max_length=500,widget=forms.TextInput(attrs={
        "class":"form-control", "placeholder":" relastion with contact person"
    }))
    alternative_contact_number = forms.CharField(max_length=500,widget=forms.TextInput(attrs={
        "class":"form-control", "placeholder":" alternative_contact_number"
    }))
    contact_number = forms.CharField(max_length=500,widget=forms.TextInput(attrs={
        "class":"form-control", "placeholder":" contact_number"
    }))
    address = forms.CharField(max_length=500,widget=forms.TextInput(attrs={
        "class":"form-control", "placeholder":"Address"
    }))
    student_father_name = forms.CharField(max_length=500,widget=forms.TextInput(attrs={
        "class":"form-control", "placeholder":"Father name"
    }))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={
        "class":"form-control", "type":"date"
    }))
    class Meta:
        model = student
        fields = '__all__'