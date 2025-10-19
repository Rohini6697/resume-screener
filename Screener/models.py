from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    ROLL_CHOICES = (
        ('candidate','Candidate'),
        ('company','Company'),
        
    )
    full_name = models.CharField(max_length=30,null=True,blank=True)
    role = models.CharField(max_length=20,choices=ROLL_CHOICES,default='candidate')
    whatsapp_number = models.CharField(max_length=20,null=True,blank=True)
    resume = models.FileField(upload_to='resume/' ,null=True,blank=True)

def __str__(self):
    return f"{self.user.username}-{self.role}"