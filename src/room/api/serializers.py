from rest_framework import serializers

from room.models import Room


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'
        read_only_fields = ('created_by', 'updated_by', 'created_at', 'updated_at')
        extra_kwargs = {
            'room_no': {'required': False},
            'floor_no': {'required': False},
            'price': {'required': False}
        }
