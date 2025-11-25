from django.db import models
from django.contrib.auth import get_user_model
from center.models import Center, Teacher
from course.models import Course
from common.models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password, check_password

User = get_user_model()

class Application(BaseModel):
    STATUS_PENDING = 'pending'
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'

    STATUS_CHOICES = [
        (STATUS_PENDING, _('Kutilmoqda')),
        (STATUS_APPROVED, _('Tasdiqlandi')),
        (STATUS_REJECTED, _('Rad etildi')),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"{self.student} - {self.course}"



class StudentForm(BaseModel):
    EXPERIENCE_CHOICES = [
        ('new', _('Yangi')),
        ('some', _('Ozgina tajriba')),
    ]
    FORMAT_CHOICES = [
        ('online', _('Online')),
        ('offline', _('Offline')),
    ]
    LANGUAGE_CHOICES = [
        ('uzb', _("O‘zbek")),
        ('eng', _('Ingliz')),
        ('rus', _('Rus')),
    ]
    DAYS_CHOICES = [
        ('3', _('Haftasiga 3 kun')),
        ('5', _('Haftasiga 5 kun')),
    ]

    application = models.OneToOneField(Application, on_delete=models.CASCADE, related_name='form')
    full_name = models.CharField(max_length=150)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=30)
    region = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    study_days = models.CharField(max_length=2, choices=DAYS_CHOICES)
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    experience = models.CharField(max_length=10, choices=EXPERIENCE_CHOICES)
    extra_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.full_name



class LoginPassword(BaseModel):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=200)  # hashed
    is_active = models.BooleanField(default=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.student} - {self.course}"


class ApplicationStatusNotification(BaseModel):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    status = models.CharField(max_length=20, choices=Application.STATUS_CHOICES)
    status_changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Xabar: {self.application.student} → {self.application.course.name} ({self.get_status_display()})"
