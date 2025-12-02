from rest_framework import serializers

from groups.models import GroupStudent


class GroupStudetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupStudent
        fields = [
            'group',
            'student',
            'join_date',
        ]