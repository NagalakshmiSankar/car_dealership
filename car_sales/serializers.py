from rest_framework import serializers
from .models import Car, Dealer

class CarSerializer(serializers.ModelSerializer):
    ''' Serializer class for mapping Car model'''
    class Meta:
        model = Car
        fields = '__all__'
        
class DealerSerializer(serializers.ModelSerializer):
    ''' Serializer class for mapping Dealer model'''
    class Meta:
        model = Dealer
        fields = '__all__'
        
        
        