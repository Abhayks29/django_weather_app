# Project Structure Guide

## 📁 Complete Directory Structure

```
django/
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── setup.py                     # Automated setup script
├── run.sh                       # Easy run script
├── README.md                    # Full documentation
├── QUICKSTART.md                # Quick start guide
├── .env.example                 # Environment variables template
├── .gitignore                   # Git ignore rules
│
├── weatherproject/              # Main Django project settings
│   ├── __init__.py
│   ├── settings.py              # Django configuration & API key
│   ├── urls.py                  # Main URL routing
│   └── wsgi.py                  # WSGI application
│
├── weather/                     # Weather app (core functionality)
│   ├── __init__.py
│   ├── models.py                # Database models (WeatherData)
│   ├── views.py                 # API views & logic
│   ├── urls.py                  # App URL routing
│   ├── serializers.py           # DRF serializers
│   ├── admin.py                 # Django admin configuration
│   ├── apps.py                  # App configuration
│   ├── tests.py                 # Unit tests
│   └── migrations/
│       ├── __init__.py
│       └── 0001_initial.py      # Initial database schema
│
└── templates/
    └── index.html               # Frontend UI (HTML/CSS/JS)
```

## 📋 File Descriptions

### Root Files

| File | Purpose |
|------|---------|
| `manage.py` | Django CLI for running commands |
| `requirements.txt` | Python dependencies (pip install -r) |
| `setup.py` | Automated setup script |
| `run.sh` | Bash script to easily start app |
| `README.md` | Complete project documentation |
| `QUICKSTART.md` | Quick start guide with commands |
| `.env.example` | Template for environment variables |
| `.gitignore` | Files/folders to exclude from git |

### Backend (`weatherproject/`)

| File | Purpose |
|------|---------|
| `settings.py` | Django configuration, installed apps, API key |
| `urls.py` | Main URL routing to apps |
| `wsgi.py` | WSGI application entry point |

### Weather App (`weather/`)

| File | Purpose |
|------|---------|
| `models.py` | WeatherData model - stores weather info |
| `views.py` | API logic - fetches and returns weather |
| `urls.py` | Weather app URL patterns |
| `serializers.py` | Converts models to/from JSON (DRF) |
| `admin.py` | Admin panel configuration |
| `apps.py` | App metadata |
| `tests.py` | Unit tests for models and API |
| `migrations/0001_initial.py` | Database schema |

### Frontend (`templates/`)

| File | Purpose |
|------|---------|
| `index.html` | Complete UI in single HTML file |

## 🔄 Data Flow

```
User Browser
    ↓
index.html (Frontend - HTML/CSS/JS)
    ↓
fetch() → /api/weather/get_weather/?city=London
    ↓
Django URL Router (urls.py)
    ↓
WeatherViewSet.get_weather() (views.py)
    ↓
OpenWeatherMap API
    ↓
WeatherData Model (models.py) - Save to Database
    ↓
WeatherDataSerializer (serializers.py) - Convert to JSON
    ↓
API Response → Browser → Display on UI
```

## 🔑 Key Components

### 1. Models (weather/models.py)
- **WeatherData**: Stores weather information for each city
  - Fields: city, country, temperature, humidity, pressure, etc.
  - Automatically saves timestamp when created

### 2. Views (weather/views.py)
- **WeatherAPIView**: Contains logic to fetch from OpenWeatherMap API
- **WeatherViewSet**: REST API endpoints
  - `GET /api/weather/` - List all weather records
  - `GET /api/weather/get_weather/?city=X` - Get weather for a city
  - `GET /api/weather/search_history/` - Get last 10 searches

### 3. Frontend (templates/index.html)
- Beautiful responsive UI with gradient background
- Search form to enter city names
- Display current weather with all details
- Search history showing recent queries
- All CSS and JS included in single file

### 4. URLs (urls.py files)
- **weatherproject/urls.py** - Routes to home page and API
- **weather/urls.py** - Routes to WeatherViewSet endpoints

## 🌐 API Endpoints

### Weather Endpoints
```
GET  /api/weather/                          → List all weather records
GET  /api/weather/{id}/                     → Get specific weather record
GET  /api/weather/get_weather/?city=London  → Get weather for a city
GET  /api/weather/search_history/           → Get recent searches
```

### Frontend
```
GET  /                                      → Serve index.html
GET  /admin/                                → Django admin panel
```

## 🗄️ Database Schema

### WeatherData Table
```sql
id              | Integer (Primary Key)
city            | String(100)
country         | String(100)
temperature     | Float
feels_like      | Float (nullable)
humidity        | Integer (%)
pressure        | Integer (hPa)
description     | String(100)
wind_speed      | Float (m/s)
cloudiness      | Integer (%)
timestamp       | DateTime (auto-created)
```

## 🔗 Dependencies

### Django Packages
- **Django** - Web framework
- **djangorestframework** - REST API toolkit
- **requests** - HTTP library for API calls
- **python-decouple** - Environment configuration

## 🚀 Execution Flow

1. User opens `http://127.0.0.1:8000`
2. Django serves `index.html` from templates
3. User enters city name and clicks Search
4. JavaScript sends AJAX request to `/api/weather/get_weather/?city=X`
5. Django routes to WeatherViewSet.get_weather()
6. View fetches from OpenWeatherMap API using API key
7. Data saved to database via WeatherData model
8. Serialized to JSON and returned to frontend
9. JavaScript displays data on UI
10. City added to search history

## 🧪 Testing

Run tests with:
```bash
python manage.py test weather
```

Tests include:
- Model creation and validation
- API endpoint functionality
- Frontend page loading
- Search history functionality

## 📦 Static Files & Media

- **Static Files**: CSS, JS (inline in index.html)
- **Media**: Not used in this app
- **Database**: SQLite (db.sqlite3)

## 🔐 Security Notes

### For Production:
1. Change `SECRET_KEY` in settings.py
2. Set `DEBUG = False`
3. Update `ALLOWED_HOSTS`
4. Use environment variables for sensitive data
5. Add HTTPS/SSL
6. Use production database (PostgreSQL)
7. Use production web server (Gunicorn)

## 📚 Learning Resources

- **Django Docs**: https://docs.djangoproject.com/
- **Django REST Framework**: https://www.django-rest-framework.org/
- **OpenWeatherMap API**: https://openweathermap.org/api
- **Python Requests**: https://docs.python-requests.org/

## 🆘 Troubleshooting

See QUICKSTART.md for common issues and solutions.
