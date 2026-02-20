
# 🌦️ Weather App — ETL + Terminal UI + Web UI

A complete weather application that:

- Fetches real‑time weather data (ETL pipeline)  
- Stores it in a SQLite database  
- Lets users view weather in a **terminal UI** or **web UI**  
- Supports **global city search**, **fuzzy matching**, and **weather icons**  
- Includes a powerful **launcher** with diagnostics, ETL, and database tools  

This project is designed to be user‑friendly, robust, and easy to run on any machine.

---

# 📁 Project Structure

```
weather-app/
│
├── main.py              # ETL pipeline (fetch + load)
├── terminal_app.py      # Terminal UI (fuzzy search + icons + live API)
├── web_app.py           # Streamlit web UI
├── launcher.py          # Main menu (Terminal/Web/ETL/Diagnostics/Reset DB)
├── init_db.py           # Auto-creates weather.db if missing
│
├── requirements.txt     # Dependencies
├── README.md            # Documentation
│
└── weather.db           # Optional: sample database
```

---

# 🚀 Getting Started

## 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

Optional enhancements:

```
pip install rich rapidfuzz
```

- `rich` → color UI  
- `rapidfuzz` → fuzzy search  
- Both optional — the app still works without them.

---

# 🗄️ Database Handling

### ✔ Automatic database creation  
If `weather.db` is missing, the launcher will automatically run:

```
init_db.py
```

This creates the correct table structure with no user action required.

### ✔ Reset Database  
The launcher includes a safe option to:

- Delete `weather.db`  
- Recreate it cleanly  

Useful for testing or starting fresh.

---

# 🧪 Diagnostics Mode

The launcher includes a full diagnostics suite that checks:

- Required files  
- Installed dependencies  
- Database presence  
- Internet connection  
- Streamlit availability  

Example output:

```
=== Diagnostics Report ===
✔ weather.db exists
✔ terminal_app.py found
✔ requests installed
✖ rich NOT installed (optional)
✔ Internet connection OK
```

---

# 🏗️ Running the App

Use the launcher to choose your interface:

```
python launcher.py
```

You’ll see:

```
=== Weather App Launcher ===
1. Terminal Viewer
2. Web UI
3. Run ETL Now
4. Diagnostics
5. Reset Database
6. Exit
```

---

# 🖥️ Terminal Viewer Features

The terminal UI (`terminal_app.py`) includes:

### 🌍 Global City Search  
Type **any** city name:

- `tokyo`
- `new york`
- `sydney`
- `cairo`

If the city isn’t in the database, the app fetches **live weather** using Open‑Meteo.

### 🔍 Fuzzy Search  
Even messy inputs work:

- `ldn` → London  
- `brln` → Berlin  
- `ams` → Amsterdam  

### 🌤️ Weather Icons  
Weather conditions are displayed with emoji:

- ☀️ Clear sky  
- 🌧️ Rain  
- 🌨️ Snow  
- ⛈️ Thunderstorm  

### 🎨 Rich UI (optional)  
If `rich` is installed:

- Color tables  
- Borders  
- Panels  

If not installed → plain fallback.

---

# 🌐 Web UI (Streamlit)

Launch with:

```
python -m streamlit run web_app.py
```

Or choose **Web UI** from the launcher.

### ✔ Auto‑install Streamlit  
If Streamlit is missing, the launcher will offer to install it.

### ✔ Features  
- Dropdown city selector  
- Weather display  
- Clean, simple interface  

---

# 🏗️ ETL Pipeline

Run manually:

```
python main.py
```

Or choose **Run ETL Now** from the launcher.

The ETL:

- Fetches weather for predefined cities  
- Inserts data into `weather.db`  
- Updates existing entries  

---

# 🧹 Resetting the Project

To completely reset:

1. Choose **Reset Database** in the launcher  
2. Run **Run ETL Now**  
3. Launch Terminal or Web UI  

---
