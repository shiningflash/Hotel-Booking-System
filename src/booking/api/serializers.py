from rest_framework import serializers

from booking.models import Booking


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ('created_by', 'updated_by', 'created_at', 'updated_at')


class BookingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        exclude = ('created_by', 'updated_by', 'created_at', 'updated_at')
