from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    ROLL_CHOICES = (
        ('candidate','Candidate'),
        ('company','Company'),
        
    )
    role = models.CharField(max_length=20,choices=ROLL_CHOICES,default='candidate')
    def __str__(self):
        return f"{self.user.username}-{self.role}"
    


from django.db import models
from .models import Profile   # if Profile is in same app

class Candidates(models.Model):
    WORK_TYPES = (
        ('wfh', 'Work From Home'),
        ('hybrid', 'Hybrid'),
        ('onsite', 'On-site'),
    )
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='other')
    work_type = models.CharField(max_length=10, choices=WORK_TYPES, default='onsite')
    preferred_location = models.CharField(max_length=100)
    skills = models.TextField(blank=True, null=True)
    experience = models.PositiveIntegerField(default=0)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.preferred_location}"


from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)  
    # Connect company to login account

    logo = models.ImageField(upload_to='company/logos/', null=True, blank=True)

    name = models.CharField(max_length=200)
    website = models.URLField(max_length=300, null=True, blank=True)
    industry = models.CharField(max_length=200, null=True, blank=True)

    size = models.CharField(
        max_length=50,
        choices=[
            ('1-10 employees', '1-10 employees'),
            ('10-50 employees', '10-50 employees'),
            ('50-200 employees', '50-200 employees'),
            ('200-500 employees', '200-500 employees'),
            ('500+ employees', '500+ employees'),
        ],
        null=True,
        blank=True
    )

    location = models.CharField(max_length=200, null=True, blank=True)
    about = models.TextField(null=True, blank=True)

    linkedin = models.URLField(max_length=300, null=True, blank=True)
    twitter = models.URLField(max_length=300, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"





class Job(models.Model):

    JOB_LOCATION_CHOICES = (
        ('Remote', 'Remote'),
        ('Office', 'On Site'),
        ('Hybrid', 'Hybrid'),
    )

    JOB_TYPE_CHOICES = (
        ('Full-Time', 'Full-Time'),
        ('Internship', 'Internship'),
        ('Contract', 'Contract'),
    )

    EXPERIENCE_TYPE_CHOICES = (
        ('Fresher', 'Fresher'),
        ('Experienced', 'Experienced Professional'),
    )

    STATUS_CHOICES = (
        ('active', 'Active'),
        ('closed', 'Closed'),
    )

    # link job to the company profile
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=20, choices=JOB_LOCATION_CHOICES)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    experience_type = models.CharField(max_length=30, choices=EXPERIENCE_TYPE_CHOICES)

    # Only required if experience_type == Experienced
    min_experience = models.PositiveIntegerField(null=True, blank=True)
    max_experience = models.PositiveIntegerField(null=True, blank=True)

    # Salary
    min_salary = models.PositiveIntegerField(null=True, blank=True)
    max_salary = models.PositiveIntegerField(null=True, blank=True)

    skills = models.CharField(max_length=300)
    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.company.name}"
