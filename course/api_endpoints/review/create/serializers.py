from rest_framework import serializers

from course.models import Review

class ReviewCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'student',
            'course',
            'rating',
            'comment',
            'created_at'
        ]