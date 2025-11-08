from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model

from common.models import BaseModel
from account.models import User, Profile
from center.models import Center, Teacher, Subject


User = get_user_model()

class Course(BaseModel):
    FORMAT_CHOICES = (
        ('online', 'Online'),
        ('offline', 'Offline'),
    )
    LANGUAGE_CHOICES = (
        ('uzb', 'Uzb'),
        ('eng', 'Eng'),
        ('rus', 'Rus')
    )

    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL,null=True,blank=True,related_name='subject_courses')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL,null=True,blank=True,related_name='teacher_courses')
    title = models.CharField(max_length=500)
    start_time = models.DateField(null=True, blank=True)
    end_time = models.DateField(null=True, blank=True)
    schedule = models.CharField(max_length=20, choices=FORMAT_CHOICES, default='offline')
    language = models.CharField(max_length=60, choices=LANGUAGE_CHOICES, default='Uzb')
    max_student = models.PositiveBigIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Course"
        ordering = ['-start_time']
        permissions = [
            ("can_add_course", "Kurs qo'shish huquqi"),
        ]

    def __str__(self):
        return f"{self.title} | {self.get_schedule_display()} | {self.center.name}"


class Review(BaseModel):
    RATING_CHOICES = (
        (1, '1 - Juda yomon'),
        (2, '2 - Yomon'),
        (3, '3 - O‘rtacha'),
        (4, '4 - Yaxshi'),
        (5, '5 - Ajoyib'),
    )

    student = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviews')
    course = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=0)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Sharh"
        verbose_name_plural = "Comments"
        unique_together = ('student', 'course')
        ordering = ['-created_at']
        constraints = [
            models.CheckConstraint(
                check=models.Q(rating__gte=0) & models.Q(rating__lte=5),
                name='rating_0_to_5'
            )
        ]
def __str__(self):
    stars = '⭐' * self.rating
    return f"{self.student.full_name} → {self.course.name} | {stars} ({self.rating}/5)"

    def add_star(self):
        if self.rating < 5:
            self.rating += 1
            self.save(update_fields=['rating'])
        return self.rating