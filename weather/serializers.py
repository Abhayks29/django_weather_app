from rest_framework import serializers
from .models import WeatherData

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = ['id', 'city', 'country', 'temperature', 'feels_like', 'humidity', 
                  'pressure', 'description', 'wind_speed', 'cloudiness', 'timestamp']
