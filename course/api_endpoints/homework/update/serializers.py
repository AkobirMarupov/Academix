from rest_framework import serializers

from course.models import Homework


class HomeworkUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = [
            'course',
            'title',
            'files',
            'due_date',
            'is_checked'
        ]