from rest_framework import serializers

from center.models import Teacher


class TeacherListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            'id',
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
