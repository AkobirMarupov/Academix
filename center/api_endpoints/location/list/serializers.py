from rest_framework import serializers

from center.models import Location


class LocationListeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            'id',
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