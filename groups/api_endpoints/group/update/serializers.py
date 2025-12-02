from rest_framework.serializers import ModelSerializer
from groups.models import Group


class GroupUpdateSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'id',
            'name',
            'course',
            'teacher',
            'max_students',
            'schedule',
            'room_number',
            'start_time',
            'end_time',
        ]
        extra_kwargs = {
            'course': {'required': False},
            'teacher': {'required': False},
            'schedule': {'required': False},
        }