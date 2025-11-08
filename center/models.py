from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from common.models import BaseModel
from account.models import User




class Subject(BaseModel):
    LEVEL_CHOICES = [
        ('beginner', _('Boshlang‘ich')),
        ('intermediate', _('O‘rta')),
    ]

    name = models.CharField(max_length=200, unique=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.name


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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teachers')  
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    experience_years = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='teachers/images/',null=True,blank=True)
    center = models.ForeignKey('Center',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Location(models.Model):
    center = models.ForeignKey('center.Center', on_delete=models.CASCADE, related_name='locations', null=True, blank=True)
    country = models.CharField(_("Country"), max_length=100)
    city = models.CharField(_("City"), max_length=100)
    region = models.CharField(_("Region"), max_length=100, null=True, blank=True)
    address = models.CharField(_("Address"), max_length=255)
    postal_code = models.CharField(_("Postal Code"), max_length=20, null=True, blank=True)

    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    google_maps_link = models.URLField(_("Google Maps link"), max_length=500, null=True, blank=True)
    is_primary = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_locations'
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='updated_locations'
    )

    def __str__(self):
        return f"{self.city}, {self.address}"

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")
        ordering = ["-created_at"]

    

