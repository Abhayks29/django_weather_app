from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from django.conf import settings
from .models import WeatherData
from .serializers import WeatherDataSerializer
from collections import defaultdict

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

    def get_forecast_from_api(self, city):
        try:
            api_key = settings.WEATHER_API_KEY
            if api_key == 'your-openweathermap-api-key' or not api_key:
                return None

            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
            response = requests.get(url, timeout=5)

            if response.status_code != 200:
                return None

            data = response.json()
            daily = defaultdict(list)
            for item in data['list']:
                date = item['dt_txt'].split(' ')[0]
                daily[date].append(item)

            forecast = []
            for date, items in list(daily.items())[:5]:
                temps = [i['main']['temp'] for i in items]
                descriptions = [i['weather'][0]['main'] for i in items]
                forecast.append({
                    'date': date,
                    'temp_min': round(min(temps)),
                    'temp_max': round(max(temps)),
                    'description': max(set(descriptions), key=descriptions.count),
                })

            return forecast
        except Exception as e:
            print(f"❌ Forecast Error: {e}")
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
    def get_forecast(self, request):
        city = request.query_params.get('city')
        if not city:
            return Response({'error': 'City parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        weather_api = WeatherAPIView()
        forecast = weather_api.get_forecast_from_api(city)

        if forecast:
            return Response(forecast, status=status.HTTP_200_OK)
        return Response({'error': f'Forecast for {city} not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'])
    def search_history(self, request):
        """Get weather search history"""
        weather_data = WeatherData.objects.all().order_by('-timestamp')[:10]
        serializer = self.get_serializer(weather_data, many=True)
        return Response(serializer.data)
