# Generated by Django 4.1 on 2023-02-22 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=500)),
                ('student_father_name', models.CharField(max_length=500)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=500)),
                ('contact_number', models.CharField(max_length=12)),
                ('alternative_contact_number', models.CharField(max_length=12)),
                ('relastion_with_contact_person', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('student_image', models.ImageField(upload_to='student_image')),
                ('id_idcard', models.CharField(max_length=300)),
                ('police_verification', models.CharField(max_length=300)),
            ],
        ),
    ]