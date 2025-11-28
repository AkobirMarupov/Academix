from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel
from course.models import Course, Teacher
from students.models import Student
from multiselectfield import MultiSelectField


class Group(BaseModel):
    DAYS = [
        ('dushanba', 'Dushanba'),
        ('seshanba', 'Seshanba'),
        ('chorshanba', 'Chorshanba'),
        ('payshanba', 'Payshanba'),
        ('juma', 'Juma'),
        ('shanba', 'Shanba'),
        ('yakshanba', 'Yakshanba'),
    ]

    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    max_students = models.IntegerField(null=True, blank=True)
    schedule = MultiSelectField(choices=DAYS, max_length=200)
    room_number = models.IntegerField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class GroupStudent(BaseModel):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    join_date = models.DateField()

    def __str__(self):
        return f"{self.student.full_name} → {self.group.name}"


class StudentRating(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    position_in_group = models.IntegerField(null=True, blank=True)
    position_in_center = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.full_name} ({self.score})"
