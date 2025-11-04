from django.db import models
from common.models import BaseModel
from account.models import User


class Center(BaseModel):
    name = models.CharField(max_length=200, null=False, blank=False)
    phone = models.CharField(max_length= 50, null=True, blank=True)
    telegram = models.URLField(max_length=300, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    avatar = models.ImageField(upload_to='centers/avatars/',null=True,blank=True)
    bio = models.TextField(max_length=1500, null=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='centers')
    subject = models.CharField(max_length= 200, null=False, blank=False)
    

    def __str__(self):
        return self.name
    


class Teacher(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, null=True, blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='teachers/images/',null=True,blank=True)
    center = models.ForeignKey('Center',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




class Location(BaseModel):
    center = models.ForeignKey('Center',on_delete=models.CASCADE,null=True,blank=True)
    address = models.CharField(max_length=255)
    google_maps_link = models.URLField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.address
    

