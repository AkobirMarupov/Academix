from rest_framework import serializers

from center.models import Teacher


class TeacherUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            'full_name',
            "user",
            "center",
            "subjects",
            "experience_years",
            'age',
            "image",
            "bio",
        ]
        extra_kwargs = {
            "subject": {"required": False},
            "age": {"required": False},
            "image": {"required": False},
        }
