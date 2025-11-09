from rest_framework import serializers

from course.models import Review

class ReviewUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'student',
            'course',
            'rating',
            'comment',
            'created_at'
        ]