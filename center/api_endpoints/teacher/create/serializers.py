from rest_framework import serializers

from center.models import Teacher


class TeacherCreateSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = [
            "first_name",
            "last_name",
            "user",
            "center",
            "subjects",
            "experience_years",
            'age',
            "image",
            "bio",
        ]