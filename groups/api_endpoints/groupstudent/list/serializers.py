from rest_framework import serializers

from groups.models import GroupStudent


class GroupStudetListerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupStudent
        fields = [
            'id',
            'group',
            'student',
            'join_date',
        ]