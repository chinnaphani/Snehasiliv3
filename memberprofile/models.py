from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MemberProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # memshipno = models.AutoField(primary_key=True)
    # name = models.ForeignKey(User.first_name,on_delete=models.CharField)
    photo = models.ImageField(upload_to='profile_image',blank=True)
    father_name = models.CharField(max_length=45)
    mother_name = models.CharField(max_length=45)
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=45)
    nationality_choice = (
        ('India', 'India'),
        ('Others', 'Others')
    )
    nationality = models.CharField(max_length=45, choices=nationality_choice)
    gothram_choice = (
        ('gothram1', 'aruventla'),
        ('gothram2', 'dravida'),
        ('gothram3', 'test2'),
        ('gothram4', 'test3'),
        ('Others', 'Others')
    )
    gothram = models.CharField(max_length=45, choices=gothram_choice)
    subsect_choice = (
        ('subset1', 'value1'),
        ('subset1', 'value2'),
        ('subset1', 'value3'),
        ('subset1', 'value4'),
        ('Others', 'Others')
    )
    subsect = models.CharField(max_length=45, choices=subsect_choice)

    blood_group_choice = (
        ('a+', 'A+'),
        ('o+', 'O+'),
        ('b+', 'B+'),
        ('ab+', 'AB+'),
        ('a-', 'A-'),
        ('o-', 'O-'),
        ('b-', 'B-'),
        ('ab-', 'AB-')
    )
    blood_group = models.CharField(choices=blood_group_choice, max_length=5)
    phone_no = models.CharField(max_length=11, unique=True)
    marital_status_choice = (
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('separated', 'Separated'),
        ('divorced', 'Divorced'),
        ('single', 'Single')
    )
    marital_status = models.CharField(choices=marital_status_choice, max_length=10)
    job_choice = (
        ('private', 'Private'),
        ('govt', 'GovtEmployee'),
        ('student', 'Student'),
        ('business', 'Business'),
        ('housewife', 'House Wife')
    )
    job = models.CharField(choices=job_choice, max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    monthsub_paiddate = models.CharField(max_length=15,null=True)

    def __str__(self):
        return self.user.username


