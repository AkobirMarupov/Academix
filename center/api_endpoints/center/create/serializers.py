from rest_framework import serializers
from center.models import Center

class CenterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = ['id', 
                  'name', 
                  'phone', 
                  'telegram', 
                  'email', 
                  'avatar', 
                  'bio'
            ]
        read_only_fields = ['owner']