from rest_framework import serializers

from course.models import Course


class CourseCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'center',
            'owner',
            'subject',
            'teacher',
            'name',
            'start_time',
            'end_time',
            'schedule',
            'language',
            'max_student',
        ]