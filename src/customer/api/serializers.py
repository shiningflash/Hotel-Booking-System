from rest_framework import serializers

from customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ('created_by', 'updated_by', 'created_at', 'updated_at')
        extra_kwargs = {
            'phone_no': {'required': False},
            'first_name': {'required': False},
            'last_name': {'required': False}
        }


class CustomerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        exclude = ('details', 'address', 'created_by', 'updated_by', 'created_at', 'updated_at')
