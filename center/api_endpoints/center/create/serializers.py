from rest_framework import serializers
from center.models import Center

class CenterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = ['name', 'phone', 'telegram', 'email', 'avatar', 'bio', 'owner', 'subject']
        read_only_fields = ['owner']