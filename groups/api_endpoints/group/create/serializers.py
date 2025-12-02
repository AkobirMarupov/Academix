from rest_framework.serializers import ModelSerializer
from groups.models import Group


class GroupCreateSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'name',
            'course',
            'teacher',
            'max_students',
            'schedule',
            'room_number',
            'start_time',
            'end_time',
        ]