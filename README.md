# Django Weather App 🌤️

A full-featured Django weather application with a beautiful frontend and REST API backend. Get real-time weather data for any city worldwide.

## Features

✅ **Real-time Weather Data** - Fetch weather using OpenWeatherMap API
✅ **Beautiful UI** - Modern, responsive design with animations
✅ **REST API** - Complete REST API for weather operations
✅ **Search History** - View recent searches
✅ **Database Storage** - Persistent weather data storage
✅ **Auto-complete** - Click on history to refetch weather

## Tech Stack

- **Backend**: Django 4.2, Django REST Framework
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Database**: SQLite
- **Weather API**: OpenWeatherMap

## Installation & Setup

### 1. Clone and Navigate
```bash
cd /Users/enfecsolutions/Desktop/django
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Get OpenWeatherMap API Key

1. Go to https://openweathermap.org/api
2. Sign up for a free account
3. Get your API key from the dashboard
4. Update the `WEATHER_API_KEY` in `weatherproject/settings.py`

```python
WEATHER_API_KEY = 'your-api-key-here'
```

### 5. Create Database
```bash
python manage.py migrate
```

### 6. Create Superuser (Optional - for Admin Panel)
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

The app will be available at: **http://127.0.0.1:8000/**

## Usage

### Frontend
1. Open the app in your browser
2. Enter a city name in the search box
3. Click "Search" or press Enter
4. View the weather information
5. Click on recent searches to quickly fetch weather again

### API Endpoints

#### Get Weather for a City
```bash
GET /api/weather/get_weather/?city=London
```

**Response:**
```json
{
  "id": 1,
  "city": "London",
  "country": "GB",
  "temperature": 15.5,
  "feels_like": 14.2,
  "humidity": 72,
  "pressure": 1013,
  "description": "Mostly Cloudy",
  "wind_speed": 4.5,
  "cloudiness": 75,
  "timestamp": "2024-04-28T10:30:00Z"
}
```

#### Get Search History
```bash
GET /api/weather/search_history/
```

**Response:**
```json
[
  {
    "id": 1,
    "city": "London",
    "country": "GB",
    "temperature": 15.5,
    ...
  },
  ...
]
```

#### List All Weather Records
```bash
GET /api/weather/
```

## Project Structure

```
django/
├── manage.py
├── requirements.txt
├── weatherproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── weather/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
└── templates/
    └── index.html
```

## Admin Panel

Access the Django admin panel at: http://127.0.0.1:8000/admin/

Login with your superuser credentials to:
- View all weather records
- Filter by timestamp
- Search by city or country

## Troubleshooting

### Issue: "API key not valid" error
- Make sure you've set the correct OpenWeatherMap API key in settings.py
- Check that the API key is active on the OpenWeatherMap website

### Issue: City not found
- Ensure the city name is spelled correctly
- Try entering city names in English
- Check OpenWeatherMap documentation for supported city names

### Issue: Port already in use
```bash
python manage.py runserver 8001
```

## Future Enhancements

- 📍 Geolocation-based weather
- 📈 Weather forecasts (5-day, 10-day)
- 🗺️ Weather maps and radar
- 🌙 Dark mode
- 🔔 Weather alerts
- 📱 Mobile app
- 🔄 Auto-refresh functionality

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please create an issue in the repository.

# Django Weather App 🌤️

[![GitHub](https://img.shields.io/badge/GitHub-View%20Code-blue)](https://github.com/YOUR-USERNAME/django-weather-app)
[![Django](https://img.shields.io/badge/Django-4.2-green)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org/)