--
# 🌦️ Weather ETL, Terminal UI & Web UI

This project fetches real‑time weather data for major European cities using the Open‑Meteo API, stores it in a SQLite database, and lets the user view the weather in **two different interfaces**:

- A **colorized terminal UI** (with automatic fallback if Rich is not installed)  
- A **web UI** built with Streamlit  

A launcher script allows the user to choose which interface to run.  
If Streamlit is missing, the launcher can automatically install it.

---

## 📁 Project Structure

```
weather-etl/
│
├── main.py              # ETL pipeline (fetch + load)
├── terminal_app.py      # Terminal UI (Rich if installed, plain fallback + Exit option)
├── web_app.py           # Streamlit web UI
├── launcher.py          # Choose terminal or web UI (auto-installs Streamlit)
├── weather.db           # SQLite database (auto-created by ETL)
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

## ⚙️ Installation

Install all required packages:

```
pip install -r requirements.txt
```

Optional (for colorized terminal UI):

```
pip install rich
```

If Streamlit is not recognized on Windows:

```
python -m pip install streamlit
```

---

## 🏗️ Step 1 — Run the ETL Pipeline

Before using the viewers, populate the database:

```
python main.py
```

This will:

- Fetch weather for all supported European cities  
- Create `weather.db` if it doesn’t exist  
- Insert the latest weather records  

If ETL password protection is enabled, you will be prompted to enter it.

---

## 🚀 Step 2 — Choose Terminal or Web UI

Use the launcher:

```
python launcher.py
```

You will see:

```
=== Weather App Launcher ===
1. Terminal Viewer
2. Web UI
3. Exit
```

---

## 🖥️ Option 1 — Terminal Viewer

Runs a text‑based interface directly in the terminal:

```
python terminal_app.py
```

### ✔ If Rich is installed  
You get a full color UI with tables, panels, and styled output.

### ✔ If Rich is NOT installed  
The app automatically falls back to a simple plain‑text interface.

### ✔ Exit option  
Type:

- `0`  
- `exit`  
- `quit`  
- `q`  

…to leave the viewer.

---

## 🌐 Option 2 — Web UI (Streamlit)

Runs the interactive dashboard:

```
python -m streamlit run web_app.py
```

### ✔ Auto‑open browser  
The launcher forces Streamlit to open the browser automatically.

### ✔ Auto‑install Streamlit  
If Streamlit is missing, the launcher will:

1. Detect it  
2. Ask if you want to install it  
3. Install it automatically  
4. Launch the Web UI  

---

### ✔ Web UI locked to view‑only  
No deploy button, no editing, no ETL access.

---

## 📝 Notes

- Always run the ETL before using the viewers.  
- The terminal viewer and web UI are **read‑only**.  
- Rich is optional — the app works perfectly without it.  
- The launcher provides a simple, user‑friendly interface.  

---
