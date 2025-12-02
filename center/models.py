from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from common.models import BaseModel
from account.models import User


class Subject(BaseModel):
    LEVEL_CHOICES = [
        ('beginner', _('Boshlang‘ich')),
        ('intermediate', _('O‘rta')),
        ('advanced', _('Yuqori')),
    ]

    name = models.CharField(max_length=200, unique=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"

    class Meta:
        verbose_name = _("Fan")
        verbose_name_plural = _("Fanlar")
        ordering = ["name"]



class Center(BaseModel):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='owned_centers',limit_choices_to={'is_center_admin': True})
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50, null=True, blank=True)
    telegram = models.CharField(max_length=100, null=True, blank=True, help_text=_("Telegram username yoki link"))
    email = models.EmailField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(upload_to='centers/avatars/', null=True, blank=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Markaz")
        verbose_name_plural = _("Markazlar")


class Teacher(BaseModel):
    full_name = models.CharField(max_length=500, null= False, blank=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='teacher_profile',limit_choices_to={'is_teacher': True})
    center = models.ForeignKey(Center,on_delete=models.CASCADE,related_name='teachers')
    subjects = models.ManyToManyField(Subject,related_name='teachers',blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='teachers/images/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.center.name})"


    class Meta:
        verbose_name = _("O‘qituvchi")
        verbose_name_plural = _("O‘qituvchilar")
        ordering = ["-created_at"]


class Location(BaseModel):
    center = models.ForeignKey(
        Center,
        on_delete=models.CASCADE,
        related_name='locations',
        null=True,
        blank=True
    )
    country = models.CharField(_("Davlat"), max_length=100)
    city = models.CharField(_("Shahar"), max_length=100)
    region = models.CharField(_("Viloyat"), max_length=100, null=True, blank=True)
    address = models.CharField(_("Manzil"), max_length=255)
    postal_code = models.CharField(_("Pochta kodi"), max_length=20, null=True, blank=True)

    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    google_maps_link = models.URLField(_("Google Maps havola"), max_length=500, null=True, blank=True)

    is_primary = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_center_locations'
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='updated_center_locations'
    )

    def __str__(self):
        return f"{self.center.name} — {self.city}, {self.address}"

    class Meta:
        verbose_name = _("Manzil")
        verbose_name_plural = _("Manzillar")
        ordering = ["-created_at"]
