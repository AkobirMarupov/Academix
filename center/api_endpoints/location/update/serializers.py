from rest_framework import serializers

from center.models import Location


class LocationUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            'center',
            'country',
            'city',
            'region',
            'address',
            'postal_code',
            'latitude',
            'longitude',
            'google_maps_link',
            'is_primary',
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user
        return super().create(validated_data)