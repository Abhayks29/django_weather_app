# API Documentation & Testing Guide

## 🌐 API Overview

The Django Weather App provides a complete REST API for weather operations.

### Base URL
```
http://127.0.0.1:8000/api/weather/
```

### Response Format
All responses are in JSON format.

## 📍 Endpoints

### 1. Get Weather for a City
Get current weather data for a specific city.

**Request:**
```http
GET /api/weather/get_weather/?city=London
```

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| city | string | yes | City name (e.g., "London", "Paris") |

**Response (200 - Success):**
```json
{
  "id": 1,
  "city": "London",
  "country": "GB",
  "temperature": 15.5,
  "feels_like": 14.2,
  "humidity": 72,
  "pressure": 1013,
  "description": "Clouds",
  "wind_speed": 4.5,
  "cloudiness": 75,
  "timestamp": "2024-04-28T10:30:00Z"
}
```

**Response (400 - Bad Request):**
```json
{
  "error": "City parameter is required"
}
```

**Response (404 - Not Found):**
```json
{
  "error": "Weather data for InvalidCity not found"
}
```

**Example Calls:**
```bash
# Using curl
curl "http://127.0.0.1:8000/api/weather/get_weather/?city=London"

# Using Python requests
import requests
response = requests.get(
    "http://127.0.0.1:8000/api/weather/get_weather/",
    params={"city": "Paris"}
)
print(response.json())

# Using JavaScript fetch
fetch("/api/weather/get_weather/?city=Tokyo")
  .then(response => response.json())
  .then(data => console.log(data))
```

---

### 2. Search History
Get the most recent weather searches (last 10).

**Request:**
```http
GET /api/weather/search_history/
```

**Response (200 - Success):**
```json
[
  {
    "id": 1,
    "city": "London",
    "country": "GB",
    "temperature": 15.5,
    "feels_like": 14.2,
    "humidity": 72,
    "pressure": 1013,
    "description": "Clouds",
    "wind_speed": 4.5,
    "cloudiness": 75,
    "timestamp": "2024-04-28T10:30:00Z"
  },
  {
    "id": 2,
    "city": "Paris",
    "country": "FR",
    "temperature": 12.0,
    ...
  }
]
```

**Example Calls:**
```bash
# Using curl
curl "http://127.0.0.1:8000/api/weather/search_history/"

# Using Python
response = requests.get("http://127.0.0.1:8000/api/weather/search_history/")
history = response.json()
for item in history:
    print(f"{item['city']}: {item['temperature']}°C")

# Using JavaScript
fetch("/api/weather/search_history/")
  .then(r => r.json())
  .then(history => console.log(history))
```

---

### 3. List All Weather Records
Get all weather records with pagination.

**Request:**
```http
GET /api/weather/
```

**Query Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| page | integer | 1 | Page number for pagination |

**Response (200 - Success):**
```json
{
  "count": 25,
  "next": "http://127.0.0.1:8000/api/weather/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "city": "London",
      ...
    }
  ]
}
```

**Example Calls:**
```bash
# All records
curl "http://127.0.0.1:8000/api/weather/"

# Page 2
curl "http://127.0.0.1:8000/api/weather/?page=2"
```

---

### 4. Get Specific Weather Record
Get a specific weather record by ID.

**Request:**
```http
GET /api/weather/{id}/
```

**URL Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| id | integer | Weather record ID |

**Response (200 - Success):**
```json
{
  "id": 1,
  "city": "London",
  ...
}
```

**Response (404 - Not Found):**
```json
{
  "detail": "Not found."
}
```

**Example:**
```bash
curl "http://127.0.0.1:8000/api/weather/1/"
```

---

## 🧪 Testing with cURL

### Basic Weather Search
```bash
curl "http://127.0.0.1:8000/api/weather/get_weather/?city=Berlin"
```

### Multiple Cities
```bash
for city in London Paris Tokyo Dubai; do
  echo "Weather for $city:"
  curl -s "http://127.0.0.1:8000/api/weather/get_weather/?city=$city" | jq '.temperature'
done
```

### Pretty Print with jq
```bash
curl "http://127.0.0.1:8000/api/weather/get_weather/?city=Barcelona" | jq .
```

### Save Response to File
```bash
curl "http://127.0.0.1:8000/api/weather/search_history/" > weather_history.json
```

---

## 🐍 Testing with Python

```python
import requests
import json
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000/api"

# Test 1: Get weather for a city
print("Test 1: Get Weather for London")
response = requests.get(f"{BASE_URL}/weather/get_weather/", params={"city": "London"})
if response.status_code == 200:
    data = response.json()
    print(f"  ✅ {data['temperature']}°C in {data['city']}")
else:
    print(f"  ❌ Error: {response.json()}")

# Test 2: Get search history
print("\nTest 2: Get Search History")
response = requests.get(f"{BASE_URL}/weather/search_history/")
history = response.json()
print(f"  ✅ Found {len(history)} records")
for item in history[:3]:
    print(f"    - {item['city']}: {item['temperature']}°C")

# Test 3: List all records with pagination
print("\nTest 3: List All Records")
response = requests.get(f"{BASE_URL}/weather/")
data = response.json()
print(f"  ✅ Total records: {data['count']}")
print(f"  ✅ Records per page: {len(data['results'])}")

# Test 4: Error handling - missing city parameter
print("\nTest 4: Error Handling")
response = requests.get(f"{BASE_URL}/weather/get_weather/")
if response.status_code == 400:
    print(f"  ✅ Correctly returned 400: {response.json()['error']}")

# Test 5: Error handling - invalid city
print("\nTest 5: Invalid City")
response = requests.get(f"{BASE_URL}/weather/get_weather/", params={"city": "XyzInvalid"})
if response.status_code == 404:
    print(f"  ✅ Correctly returned 404: {response.json()['error']}")

print("\n✅ All tests completed!")
```

---

## 🌐 Testing with JavaScript

```javascript
// Test helper function
async function testAPI(name, url, params = {}) {
  console.log(`🧪 ${name}`);
  try {
    const queryString = new URLSearchParams(params).toString();
    const fullUrl = queryString ? `${url}?${queryString}` : url;
    
    const response = await fetch(fullUrl);
    const data = await response.json();
    
    if (response.ok) {
      console.log(`✅ Success:`, data);
    } else {
      console.log(`❌ Error:`, data);
    }
  } catch (error) {
    console.error(`❌ ${error.message}`);
  }
}

// Run tests
async function runTests() {
  const baseUrl = "/api/weather";
  
  // Test 1: Get weather
  await testAPI(
    "Get Weather for London",
    `${baseUrl}/get_weather/`,
    { city: "London" }
  );
  
  // Test 2: Search history
  await testAPI("Get Search History", `${baseUrl}/search_history/`);
  
  // Test 3: List all
  await testAPI("List All Records", baseUrl);
  
  // Test 4: Get by ID
  await testAPI("Get Record by ID", `${baseUrl}/1/`);
}

// Run the tests
runTests();
```

---

## 📊 Data Fields Explained

| Field | Unit | Example | Description |
|-------|------|---------|-------------|
| city | text | London | City name |
| country | text | GB | Country code |
| temperature | °C | 15.5 | Current temperature |
| feels_like | °C | 14.2 | Feels like temperature |
| humidity | % | 72 | Relative humidity |
| pressure | hPa | 1013 | Atmospheric pressure |
| description | text | Clouds | Weather condition |
| wind_speed | m/s | 4.5 | Wind speed |
| cloudiness | % | 75 | Cloud coverage |
| timestamp | ISO 8601 | 2024-04-28T10:30:00Z | Record creation time |

---

## 🔍 Filtering & Sorting

### Current Limitations
- The API returns records sorted by timestamp (newest first)
- Pagination is available with 100 records per page

### Future Enhancements
- Filter by city, country, date range
- Sort by temperature, humidity, etc.
- Advanced search capabilities

---

## ✅ Response Status Codes

| Code | Meaning | Example Scenario |
|------|---------|------------------|
| 200 | OK | Successful weather fetch |
| 400 | Bad Request | Missing city parameter |
| 404 | Not Found | City doesn't exist |
| 500 | Server Error | API key invalid |

---

## 🔐 API Key Configuration

The API requires an OpenWeatherMap API key.

### How to Get It:
1. Visit: https://openweathermap.org/api
2. Sign up for free account
3. Go to API keys section
4. Copy your API key
5. Add to `weatherproject/settings.py`:
```python
WEATHER_API_KEY = 'your-key-here'
```

### API Key Limits (Free Tier):
- 1000 calls per day
- 60 calls per minute
- Real-time weather data

---

## 🐛 Debugging Tips

### Enable Verbose Mode
```bash
curl -v "http://127.0.0.1:8000/api/weather/get_weather/?city=London"
```

### Check Django Logs
```bash
# See server output in terminal where runserver is running
# Shows full error traces for 500 errors
```

### Use Django Debug Toolbar
Add to installed apps in settings.py:
```python
'debug_toolbar',
```

### Test with Postman
1. Download Postman: https://www.postman.com/downloads/
2. Create new request
3. Set method to GET
4. Enter URL: http://127.0.0.1:8000/api/weather/get_weather/
5. Add param: city = London
6. Send

---

## 📝 Example Integration Code

### React Component
```javascript
import { useState, useEffect } from 'react';

function WeatherComponent() {
  const [weather, setWeather] = useState(null);
  const [city, setCity] = useState('London');
  
  const fetchWeather = async () => {
    try {
      const response = await fetch(
        `/api/weather/get_weather/?city=${city}`
      );
      const data = await response.json();
      setWeather(data);
    } catch (error) {
      console.error('Error:', error);
    }
  };
  
  return (
    <div>
      <input onChange={e => setCity(e.target.value)} />
      <button onClick={fetchWeather}>Search</button>
      {weather && (
        <div>
          <h2>{weather.city}</h2>
          <p>Temperature: {weather.temperature}°C</p>
        </div>
      )}
    </div>
  );
}
```

### Vue Component
```javascript
data() {
  return {
    city: 'London',
    weather: null
  }
},
methods: {
  async fetchWeather() {
    const res = await fetch(`/api/weather/get_weather/?city=${this.city}`);
    this.weather = await res.json();
  }
}
```

---

## 📞 Support

For API issues:
1. Check OpenWeatherMap API key is valid
2. Verify city name is correct
3. Check network connectivity
4. Review Django logs for errors
5. Consult documentation

