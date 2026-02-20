## Weather Dashboard
 
A cross‑platform weather data pipeline and dashboard built with Python.
It fetches live weather data for European cities, stores it in SQLite, and provides both a terminal interface and a Streamlit web UI for viewing conditions in Celsius and Fahrenheit, complete with icons + text descriptions.

The project includes:
ETL pipeline (Open‑Meteo API → SQLite)
Terminal weather viewer with fuzzy search
Streamlit dashboard
Docker support
Full unittest test suite
Makefile (Linux/macOS)
Windows automation script (make.bat)
Weather icons + text fallback
Celsius + Fahrenheit support

##  Features at a Glance
##  ETL Pipeline
Fetches live weather for 40+ European cities
Stores:
Temperature (°C + °F)
Weather description (icon + text)
Timestamp
Saves everything to SQLite (weather.db)


##  Terminal App
Fuzzy search for any city
Falls back to live API lookup if not in DB
Optional Rich‑formatted output
Shows °C / °F, icons, and text conditions

## Streamlit Web Dashboard
Browse stored weather
Perform live lookups
Displays:
Temperature (°C / °F)
Weather icons + text
Humidity
Wind speed

##  Testing
Full unittest suite
Windows‑safe SQLite handling

Tests for:
Weather mapping
Temperature conversion
ETL DB writes
Terminal fuzzy search
Web DB helpers

##  Docker Support
Build and run ETL, terminal, or web UI inside Docker

## ⚙ Automation
Makefile (Linux/macOS)

make.bat (Windows)

## Installation (Download Only — No Git Required)

Download the project
https://github.com/karthic180/weatherdashboard

Click: Code → Download ZIP

Unzip it anywhere on your computer.

Open a terminal in the project folder
Windows (PowerShell)

powershell
cd path\to\weatherdashboard
macOS / Linux

bash
cd path/to/weatherdashboard
 (Optional) Create a virtual environment
Windows

cmd
python -m venv venv
venv\Scripts\activate
macOS / Linux

bash
python3 -m venv venv
source venv/bin/activate
4. Install dependencies
bash
pip install -r requirements.txt
5. Run the apps
ETL Pipeline

bash
python main.py
Terminal App

bash
python terminal_app.py
Streamlit Web Dashboard

bash
streamlit run web_app.py


##  Commands
Linux/macOS (Makefile)
bash
make etl
make terminal
make web
make test
make reset-db
make docker-build
make docker-web

Windows (make.bat)
cmd
make etl
make terminal
make web
make test
make reset-db
make docker-build
make docker-web

##  Docker
Build the image
bash
docker build -t weatherapp .
Run ETL
bash
docker run weatherapp python main.py
Run Terminal App
bash
docker run -it weatherapp python terminal_app.py
Run Web UI
bash
docker run -p 8501:8501 weatherapp streamlit run web_app.py

##  Running Tests (unittest)
Discover and run all tests
bash
python -m unittest discover -v
Or explicitly:
bash
python -m unittest discover -s tests -p "test_*.py" -v

##  Project Structure

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
    
##  Configuration
Weather Mapping
Each weather code maps to:
An emoji icon
A text description

Example:
Code
🌧️ Rain
☀️ Clear sky
⛈️ Thunderstorm

Temperature Conversion
Stored in DB as both °C and °F
Displayed in both terminal and web UI

##  Requirements
Python 3.10+
Streamlit
Requests
Rich (optional)
RapidFuzz (optional)
Docker (optional)

##  License
MIT License — free to use, modify, and distribute.
