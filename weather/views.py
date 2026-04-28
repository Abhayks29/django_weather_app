from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from django.conf import settings
from .models import WeatherData
from .serializers import WeatherDataSerializer
import json

class WeatherAPIView(APIView):
    def get_weather_from_api(self, city):
        """Fetch weather data from OpenWeatherMap API"""
        try:
            api_key = settings.WEATHER_API_KEY
            
            # Check if API key is set
            if api_key == 'your-openweathermap-api-key' or not api_key:
                print(f"❌ ERROR: API key not configured! Please set WEATHER_API_KEY in settings.py")
                return None
            
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            print(f"🌐 Fetching: {url}")
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Success: Got weather data for {data['name']}")
                return {
                    'city': data['name'],
                    'country': data['sys'].get('country', ''),
                    'temperature': data['main']['temp'],
                    'feels_like': data['main'].get('feels_like', None),
                    'humidity': data['main']['humidity'],
                    'pressure': data['main']['pressure'],
                    'description': data['weather'][0]['main'],
                    'wind_speed': data['wind']['speed'],
                    'cloudiness': data['clouds']['all'],
                }
            else:
                error_data = response.json()
                print(f"❌ API Error ({response.status_code}): {error_data.get('message', 'Unknown error')}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"❌ Network Error: {e}")
            return None
        except Exception as e:
            print(f"❌ Unexpected Error: {e}")
            return None

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    
    @action(detail=False, methods=['get'])
    def get_weather(self, request):
        """Get weather for a specific city"""
        city = request.query_params.get('city')
        
        if not city:
            return Response(
                {'error': 'City parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        weather_api = WeatherAPIView()
        weather_data = weather_api.get_weather_from_api(city)
        
        if weather_data:
            # Save to database
            obj, created = WeatherData.objects.update_or_create(
                city=weather_data['city'],
                defaults=weather_data
            )
            serializer = self.get_serializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {'error': f'Weather data for {city} not found'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=False, methods=['get'])
    def search_history(self, request):
        """Get weather search history"""
        weather_data = WeatherData.objects.all().order_by('-timestamp')[:10]
        serializer = self.get_serializer(weather_data, many=True)
        return Response(serializer.data)
