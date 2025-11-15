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
    


class Candidates(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    # preferred_job = models.CharField(max_length=100)
    preferred_location = models.CharField(max_length=100)
    skills = models.TextField(blank=True, null=True)
    experience = models.PositiveIntegerField(default=0)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    def __str__(self):
        return f"{self.user.username} - {self.preferred_job}"