# 🌤️ Installation and Getting Started

## Quick Start (5 Minutes)

### Step 1️⃣ Install Dependencies
```bash
cd /Users/enfecsolutions/Desktop/django
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 2️⃣ Setup Database
```bash
python manage.py migrate
```

### Step 3️⃣ Get Weather API Key
1. Visit: https://openweathermap.org/api
2. Sign up for free account  
3. Get your API key
4. Edit `weatherproject/settings.py` and replace:
   ```python
   WEATHER_API_KEY = 'your-actual-api-key-here'
   ```

### Step 4️⃣ Run the App
```bash
python manage.py runserver
```

### Step 5️⃣ Open in Browser
Visit: **http://127.0.0.1:8000**

---

## 📋 What You Get

✅ **Beautiful Frontend** - Modern responsive UI with animations
✅ **REST API** - Complete API for weather operations  
✅ **Database** - SQLite database to store search history
✅ **Admin Panel** - Django admin at `/admin`
✅ **Real Data** - Live weather from OpenWeatherMap

---

## 🗂️ Project Files

| File/Folder | Purpose |
|-------------|---------|
| `manage.py` | Django command runner |
| `requirements.txt` | Python dependencies |
| `weatherproject/` | Django project settings |
| `weather/` | Weather app (models, views, API) |
| `templates/index.html` | Frontend UI |
| `README.md` | Complete documentation |
| `API_DOCUMENTATION.md` | Full API reference |
| `QUICKSTART.md` | Quick reference guide |
| `PROJECT_STRUCTURE.md` | Project structure overview |

---

## 🔑 Key URLs

| URL | Purpose |
|-----|---------|
| http://localhost:8000 | Main app |
| http://localhost:8000/admin | Admin panel |
| http://localhost:8000/api/weather/ | API list |
| http://localhost:8000/api/weather/get_weather/?city=London | Get weather |
| http://localhost:8000/api/weather/search_history/ | Search history |

---

## 🧪 Testing the App

### Test 1: Using the UI
1. Open http://127.0.0.1:8000
2. Type a city name (e.g., "London")
3. Click Search
4. See weather data displayed

### Test 2: Using curl
```bash
curl "http://127.0.0.1:8000/api/weather/get_weather/?city=Paris"
```

### Test 3: Using Python
```python
import requests
r = requests.get("http://127.0.0.1:8000/api/weather/get_weather/", 
                 params={"city": "Tokyo"})
print(r.json())
```

---

## 🛠️ Common Commands

### Activate Virtual Environment
```bash
source venv/bin/activate
```

### Deactivate Virtual Environment
```bash
deactivate
```

### Create Admin User
```bash
python manage.py createsuperuser
```

### Run Database Migrations
```bash
python manage.py migrate
```

### Create New Database Migration
```bash
python manage.py makemigrations
```

### Run Tests
```bash
python manage.py test weather
```

### Clear Database
```bash
rm db.sqlite3
python manage.py migrate
```

### Open Django Shell
```bash
python manage.py shell
```

### Run on Custom Port
```bash
python manage.py runserver 8001
```

---

## 🐛 Troubleshooting

### ❌ "ModuleNotFoundError: No module named 'django'"
**Fix:** Run `pip install -r requirements.txt`

### ❌ "API key not valid"
**Fix:** Check your OpenWeatherMap API key in `weatherproject/settings.py`

### ❌ "Port 8000 already in use"
**Fix:** Run on different port: `python manage.py runserver 8001`

### ❌ "City not found"
**Fix:** Check spelling, try different city name

### ❌ Database errors
**Fix:** Delete `db.sqlite3` and run `python manage.py migrate`

### ❌ Static files not loading
**Fix:** Run `python manage.py collectstatic`

---

## 📦 Requirements

- Python 3.8+
- pip (Python package manager)
- Internet connection (for OpenWeatherMap API)
- Web browser

---

## 🚀 Project Features

### Frontend Features
- 🔍 City search with autocomplete
- 🌡️ Current temperature display
- 💧 Humidity, pressure, wind speed
- ☁️ Cloud coverage and weather description
- 📱 Mobile responsive design
- 🎨 Beautiful gradient UI
- 📊 Search history
- ⚡ Real-time updates

### Backend Features
- 📡 REST API endpoints
- 💾 SQLite database
- 🔐 Admin panel
- 🧪 Unit tests
- 🌐 OpenWeatherMap integration
- 📈 Pagination support
- 🔍 Search history tracking

---

## 📚 Documentation Files

1. **README.md** - Full project documentation
2. **QUICKSTART.md** - Quick reference and common tasks
3. **PROJECT_STRUCTURE.md** - Detailed file structure explanation
4. **API_DOCUMENTATION.md** - Complete API reference with examples
5. **INSTALLATION.md** - This file (installation guide)

---

## 💡 Tips

- Use the Django admin panel to view all weather records
- Click on search history to quickly refetch weather
- Check the API docs for programmatic access
- Set up a cronjob to regularly fetch weather
- Deploy to cloud platforms like Heroku, AWS, or DigitalOcean

---

## 🆘 Getting Help

### Check Documentation
- Full docs: [README.md](README.md)
- Quick guide: [QUICKSTART.md](QUICKSTART.md)
- API reference: [API_DOCUMENTATION.md](API_DOCUMENTATION.md)
- Project structure: [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)

### External Resources
- Django: https://docs.djangoproject.com/
- DRF: https://www.django-rest-framework.org/
- OpenWeatherMap: https://openweathermap.org/api
- Python: https://python.org/

---

## ✨ Next Steps

1. ✅ Install dependencies and setup database
2. 🔑 Get OpenWeatherMap API key
3. ▶️ Run the development server
4. 🌐 Open the app in browser
5. 🧪 Test the API endpoints
6. 🚀 Deploy to production (optional)

**Ready to go! Enjoy your weather app! 🌤️**
