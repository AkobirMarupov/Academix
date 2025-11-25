from rest_framework import serializers

from course.models import Homework


class HomeworkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = [
            'id',
            'course',
            'title',
            'files',
            'due_date',
            'is_checked'
        ]