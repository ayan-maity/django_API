from rest_framework import serializers
from .models import orderhistory
from .models import itemcatalog


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = orderhistory
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = itemcatalog
        fields = '__all__'
