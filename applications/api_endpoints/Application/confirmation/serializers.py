from rest_framework import serializers
from applications.models import Application


class ApplicationConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['status']

        extra_kwargs = {
            'status': {'required': True}
        }