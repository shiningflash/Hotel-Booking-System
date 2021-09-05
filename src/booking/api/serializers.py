from rest_framework import serializers

from booking.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField()
    updated_by = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()

    class Meta:
        model = Booking
        fields = '__all__'
