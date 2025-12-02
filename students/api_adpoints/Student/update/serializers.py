from rest_framework import serializers

from students.models import Student

class StudentUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'user',
            'full_name',
            'phone',
            'birth_date',
            'address',
        ]

        extra_kwargs = {
            'user': {'required': False},
        }