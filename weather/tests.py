from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import WeatherData
import json


class WeatherDataModelTest(TestCase):
    """Test WeatherData model"""
    
    def setUp(self):
        self.weather = WeatherData.objects.create(
            city="London",
            country="GB",
            temperature=15.5,
            feels_like=14.2,
            humidity=72,
            pressure=1013,
            description="Cloudy",
            wind_speed=4.5,
            cloudiness=75
        )
    
    def test_weather_creation(self):
        """Test weather data creation"""
        self.assertEqual(self.weather.city, "London")
        self.assertEqual(self.weather.temperature, 15.5)
        self.assertEqual(self.weather.humidity, 72)
    
    def test_weather_string_representation(self):
        """Test weather model __str__ method"""
        self.assertEqual(str(self.weather), "London - 15.5°C")
    
    def test_weather_ordering(self):
        """Test weather data is ordered by timestamp descending"""
        weather2 = WeatherData.objects.create(
            city="Paris",
            country="FR",
            temperature=12.0,
            feels_like=11.0,
            humidity=65,
            pressure=1010,
            description="Rainy",
            wind_speed=5.0,
            cloudiness=90
        )
        
        weathers = WeatherData.objects.all()
        self.assertEqual(weathers[0].city, "Paris")
        self.assertEqual(weathers[1].city, "London")


class WeatherAPITest(APITestCase):
    """Test Weather API endpoints"""
    
    def setUp(self):
        self.client = Client()
        self.weather = WeatherData.objects.create(
            city="London",
            country="GB",
            temperature=15.5,
            feels_like=14.2,
            humidity=72,
            pressure=1013,
            description="Cloudy",
            wind_speed=4.5,
            cloudiness=75
        )
    
    def test_weather_list_endpoint(self):
        """Test GET /api/weather/"""
        response = self.client.get('/api/weather/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('results', response.json() or response.json().get('results'))
    
    def test_get_weather_without_city_parameter(self):
        """Test get_weather without city parameter"""
        response = self.client.get('/api/weather/get_weather/')
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)
    
    def test_search_history_endpoint(self):
        """Test GET /api/weather/search_history/"""
        response = self.client.get('/api/weather/search_history/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
    
    def test_weather_retrieve_endpoint(self):
        """Test GET /api/weather/{id}/"""
        response = self.client.get(f'/api/weather/{self.weather.id}/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['city'], 'London')
        self.assertEqual(data['temperature'], 15.5)


class FrontendTest(TestCase):
    """Test frontend page"""
    
    def setUp(self):
        self.client = Client()
    
    def test_index_page_loads(self):
        """Test that index page loads"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Weather App', response.content)
        self.assertIn(b'Enter city name', response.content)
    
    def test_index_page_has_search_form(self):
        """Test that index page has search elements"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'cityInput', response.content)
        self.assertIn(b'searchWeather', response.content)


# Run tests with: python manage.py test weather
