

# Weather Dashboard

A cross‑platform weather data pipeline and dashboard built with Python.  
It fetches live weather data for European cities, stores it in SQLite, and provides both a terminal interface and a Streamlit web UI for viewing conditions in Celsius and Fahrenheit, with text descriptions.

---

## Project Includes

- ETL pipeline (Open‑Meteo API → SQLite)  
- Terminal weather viewer with fuzzy search  
- Streamlit dashboard  
- Docker support  
- Full unittest test suite  
- Makefile (Linux/macOS)  
- Windows automation script (`make.bat`)  
- Celsius + Fahrenheit support  

---

##  Features at a Glance

###  ETL Pipeline
- Fetches live weather for 40+ European cities  
- Stores:
  - Temperature (°C and °F)  
  - Weather description (text)  
  - Timestamp  
- Saves all data to SQLite (`weather.db`)

---

### Terminal App
- Fuzzy search for any city  
- Falls back to live API lookup if city not in DB  
- Optional Rich‑formatted output  
- Displays °C/°F and text weather conditions  

**Example Terminal Output:**
```
Weather for Berlin:
Temperature: 18°C / 64°F
Conditions: Clear sky
Humidity: 55%
Wind Speed: 12 km/h
```

---

###  Streamlit Web Dashboard
- Browse stored weather  
- Perform live lookups  
- Displays:
  - Temperature (°C / °F)  
  - Weather description  
  - Humidity  
  - Wind speed  

**Example Web UI Output:**
```
City: Paris
Temperature: 21°C / 70°F
Conditions: Partly cloudy
Humidity: 48%
Wind Speed: 10 km/h
```

---

#  Screenshots

##  Web Dashboard (Streamlit)


```
┌──────────────────────────────────────────────────────────────────────────────┐
│                           🌦 Weather Dashboard                               │
├──────────────────────────────────────────────────────────────────────────────┤
│ City Lookup                                                                  │
│ [ Berlin ____________________________ ]   (Search)                            │
│                                                                              │
│ ──────────────────────────────────────────────────────────────────────────── │
│ 📍 City: Berlin                                                               │
│ 🌡 Temperature: 10°C / 50°F                                                   │
│ 🌦 Condition: ☁️ Overcast                                                      │
│ 💧 Humidity: 82%                                                              │
│ 💨 Wind Speed: 5.2 m/s                                                        │
│ 🕒 Timestamp: 2024‑01‑01 12:00 UTC                                             │
│                                                                              │
│ ──────────────────────────────────────────────────────────────────────────── │
│ Recent Stored Weather                                                         │
│                                                                              │
│  City       Temp (°C)   Temp (°F)   Condition        Time                     │
│  ─────────  ─────────   ─────────   ─────────────    ─────────────────────   │
│  London     12          53.6        🌧️ Rain          2024‑01‑01 11:00 UTC     │
│  Paris      14          57.2        ☁️ Overcast       2024‑01‑01 11:00 UTC     │
│  Rome       18          64.4        ☀️ Clear sky      2024‑01‑01 11:00 UTC     │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

##  Terminal App

```
===========================================
        🌦  Weather Lookup (Terminal)
===========================================

Enter a city: berlin

City: Berlin
Temperature: 10°C / 50°F
Condition: ☁️ Overcast
Humidity: 82%
Wind Speed: 5.2 m/s
Timestamp: 2024‑01‑01 12:00 UTC

===========================================
```

---

##  Docker Support

- Build and run ETL, terminal, or web UI inside Docker

---

## Automation

- Makefile (Linux/macOS)  
- `make.bat` (Windows)

---

#  Installation (Download Only — No Git Required)

### 1. Download the project  
Go to:  
https://github.com/karthic180/weatherdashboard  
Click **Code → Download ZIP**

### 2. Unzip it anywhere on your computer

### 3. Open a terminal in the project folder

**Windows (PowerShell)**  
```
cd path\to\weatherdashboard
```

**macOS / Linux**  
```
cd path/to/weatherdashboard
```

### 4. (Optional) Create a virtual environment

**Windows**  
```
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**  
```
python3 -m venv venv
source venv/bin/activate
```

### 5. Install dependencies
```
pip install -r requirements.txt
```

### 6. Run the apps

**ETL Pipeline**  
```
python main.py
```

**Terminal App**  
```
python terminal_app.py
```

**Streamlit Web Dashboard**  
```
streamlit run web_app.py
```

---

#  Commands

### Linux/macOS (Makefile)
```
make etl
make terminal
make web
make test
make reset-db
make docker-build
make docker-web
```

### Windows (make.bat)
```
make etl
make terminal
make web
make test
make reset-db
make docker-build
make docker-web
```

---

#  Docker

**Build the image**
```
docker build -t weatherapp .
```

**Run ETL**
```
docker run weatherapp python main.py
```

**Run Terminal App**
```
docker run -it weatherapp python terminal_app.py
```

**Run Web UI**
```
docker run -p 8501:8501 weatherapp streamlit run web_app.py
```

---

#  Running Tests (unittest)

**Run all tests**
```
python -m unittest discover -v
```

**Or explicitly**
```
python -m unittest discover -s tests -p "test_*.py" -v
```

---

#  Project Structure

```
weatherdashboard/
    main.py
    terminal_app.py
    web_app.py
    launcher.py
    Dockerfile
    requirements.txt
    Makefile
    make.bat
    .gitignore
    tests/
        __init__.py
        test_weather_mapping.py
        test_temperature_conversion.py
        test_etl.py
        test_terminal_helpers.py
        test_web_helpers.py
```

---

#  Configuration

### Weather Mapping
Each weather code maps to a text description, e.g.:

```
Rain
Clear sky
Thunderstorm
```

### Temperature Conversion
- Stored in DB as both °C and °F  
- Displayed in both terminal and web UI  

---

#  Requirements

- Python 3.10+  
- Streamlit  
- Requests  
- Rich (optional)  
- RapidFuzz (optional)  
- Docker (optional)  

---

#  License

MIT License — free to use, modify, and distribute.

