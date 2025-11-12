from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model

from common.models import BaseModel
from account.models import Profile
from center.models import Center, Teacher, Subject

User = get_user_model()

class Course(BaseModel):
    FORMAT_CHOICES = (
        ('online', 'Online'),
        ('offline', 'Offline'),
    )
    LANGUAGE_CHOICES = (
        ('uzb', 'Uzbek'),
        ('eng', 'English'),
        ('rus', 'Russian')
    )

    center = models.ForeignKey(Center, on_delete=models.CASCADE, related_name='courses')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_courses')
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')
    name = models.CharField(max_length=60)
    start_time = models.DateField(null=True, blank=True)
    end_time = models.DateField(null=True, blank=True)
    schedule = models.CharField(max_length=20, choices=FORMAT_CHOICES, default='offline')
    language = models.CharField(max_length=60, choices=LANGUAGE_CHOICES, default='uzb')
    max_student = models.PositiveBigIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"
        ordering = ['-start_time']
        permissions = [
            ("can_add_course", "Kurs qo'shish huquqi"),
        ]

    def __str__(self):
        return f"{self.name} | {self.get_schedule_display()} | {self.center.name}"


class Review(BaseModel):
    RATING_CHOICES = (
        (1, '1 - Juda yomon'),
        (2, '2 - Yomon'),
        (3, '3 - O‘rtacha'),
        (4, '4 - Yaxshi'),
        (5, '5 - Ajoyib'),
    )

    student = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviews')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    comment = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Sharh"
        verbose_name_plural = "Sharhlar"
        unique_together = ('student', 'course')
        ordering = ['-created_at']

    def __str__(self):
        stars = '⭐' * self.rating
        return f"{self.student.full_name} → {self.course.name} | {stars} ({self.rating}/5)"

    def add_star(self):
        if self.rating < 5:
            self.rating += 1
            self.save(update_fields=['rating'])
        return self.rating
    
    
class Homework(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='homeworks')
    title = models.CharField(max_length=255)
    files = models.FileField(blank=True, null=True)
    due_date = models.DateField(null=True, blank=True)
    is_checked = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Uyga vazifa"
        verbose_name_plural = "Uyga vazifalar"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.course.name})"
