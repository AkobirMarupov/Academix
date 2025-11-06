from rest_framework import serializers

from center.models import Teacher


class TeacherUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            "first_name",
            "last_name",
            "subject",
            "experience_years",
            "age",
            "image",
            "center",
        ]
        extra_kwargs = {
            "subject": {"required": False},
            "age": {"required": False},
            "image": {"required": False},
        }
