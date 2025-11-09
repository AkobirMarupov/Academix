from rest_framework import serializers

from course.models import Review

class ReviewListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'student',
            'course',
            'rating',
            'comment',
            'created_at'
        ]