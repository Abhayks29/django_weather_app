# Quick Start Guide

## 🚀 Get the App Running in 5 Minutes

### Step 1: Navigate to Project
```bash
cd /Users/enfecsolutions/Desktop/django
```

### Step 2: Set Up Python Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Get Your Weather API Key

Visit: https://openweathermap.org/api
- Sign up for free account
- Get your API key

### Step 5: Configure API Key

Edit `weatherproject/settings.py` and replace:
```python
WEATHER_API_KEY = 'your-api-key-here'
```

### Step 6: Initialize Database
```bash
python manage.py migrate
```

### Step 7: Create Admin User (Optional)
```bash
python manage.py createsuperuser
```

### Step 8: Run the App
```bash
python manage.py runserver
```

### Step 9: Open in Browser
Visit: http://127.0.0.1:8000

## 🧪 Testing the API

### Test 1: Get Weather for London
```bash
curl "http://127.0.0.1:8000/api/weather/get_weather/?city=London"
```

### Test 2: Get Search History
```bash
curl "http://127.0.0.1:8000/api/weather/search_history/"
```

### Test 3: List All Records
```bash
curl "http://127.0.0.1:8000/api/weather/"
```

## 📊 Using the Admin Panel
1. Go to: http://127.0.0.1:8000/admin/
2. Login with superuser credentials
3. View, filter, and search weather records

## 🆘 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'django'` | Run: `pip install -r requirements.txt` |
| "API key not valid" | Check your OpenWeatherMap API key in settings.py |
| Port 8000 already in use | Run: `python manage.py runserver 8001` |
| City not found error | Try using English city names |
| Database error | Delete `db.sqlite3` and run: `python manage.py migrate` |

## 📁 File Structure

```
project/
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── README.md              # Full documentation
├── QUICKSTART.md          # This file
├── weatherproject/        # Main project settings
│   ├── settings.py        # Configuration & API key
│   ├── urls.py            # URL routing
│   ├── wsgi.py            # WSGI server config
│   └── __init__.py
├── weather/               # Main weather app
│   ├── models.py          # Database models
│   ├── views.py           # API views
│   ├── urls.py            # App URL routing
│   ├── serializers.py     # DRF serializers
│   ├── admin.py           # Admin configuration
│   ├── apps.py            # App config
│   ├── migrations/        # Database migrations
│   └── __init__.py
├── templates/             # Frontend
│   └── index.html         # Main UI
└── db.sqlite3             # Database (created after migrate)
```

## ✨ Features

- 🔍 Search weather by city name
- 🌡️ Real-time temperature and conditions
- 💧 Humidity, pressure, and wind speed
- ☁️ Cloudiness percentage
- 📱 Responsive mobile-friendly design
- 🎨 Beautiful gradient UI
- 📊 Search history tracking
- 🔗 REST API for programmatic access
- 👨‍💼 Django Admin Panel

## 🎯 Next Steps

1. Get your OpenWeatherMap API key
2. Update `weatherproject/settings.py`
3. Run `python manage.py migrate`
4. Run `python manage.py runserver`
5. Open http://127.0.0.1:8000 and enjoy!

## 📞 Need Help?

- Django Docs: https://docs.djangoproject.com/
- DRF Docs: https://www.django-rest-framework.org/
- OpenWeatherMap: https://openweathermap.org/api
