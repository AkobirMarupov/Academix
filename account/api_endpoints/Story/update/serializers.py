from rest_framework import serializers

from account.models import Story


class StoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = [
            'user',
            'title',
            'description',
            'image',
            'video',
            'is_active',
            'expires_at'
        ]