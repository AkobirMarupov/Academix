from rest_framework import serializers

from center.models import Center


class CenterUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = ['id', 'name', 'phone', 'telegram', 'email', 'avatar', 'bio', 'owner', 'subjects']
        read_only_fields = ['owner']
        extra_kwargs = {
    "name": {"required": False},
    "bio": {"required": False},
    "subject": {"required": False},

}