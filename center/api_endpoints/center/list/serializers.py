from rest_framework import serializers
from center.models import Center

class CenterLisSerializers(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = ['id', 'name', 'phone', 'telegram', 'email', 'avatar', 'bio', 'owner', 'subject']
      