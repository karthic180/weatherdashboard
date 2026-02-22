# 🌦️ Weather Dashboard  
A simple, fast, no‑signup weather dashboard with:

- **Web UI (Streamlit)**
- **Terminal CLI**
- **SQLite caching**
- **Free Open‑Meteo API**
- **Auto‑delete cache on web launch**
- **Minimal, clean UI**
- **Plain‑text loading**
- **Launcher menu**
- **Pytest test suite**

Built to run smoothly in **VS Code**

---


## 🚀 Features

### ✔ Web Dashboard  
- Clean, modern UI  
- Plain‑text “Loading weather…”  
- Diagnostics panel  
- Auto‑search on Enter  
- Clear Cache button  
- No Streamlit header/footer  
- Auto‑delete `weather.db` on launch  

### ✔ Terminal App  
- Simple CLI  
- Plain‑text output  
- Uses same SQLite cache  
- Fast and lightweight  

### ✔ Caching  
- SQLite database  
- Auto‑created  
- Auto‑deleted on web launch  
- 30‑minute expiry  

### ✔ Free API  
Uses **Open‑Meteo** — no API key required.

---

## 🛠 Installation

```bash
git clone
cd weatherdashboard
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

---

## ▶️ Running the App

### **Launcher Menu**
```bash
python launcher.py
```

Menu options:

```
1) Run Terminal App
2) Run Web Dashboard
0) Exit
```

### Web Dashboard  
Opens in your browser and returns instantly to PowerShell/CMD.

### Terminal App  
Runs directly in your console.

---

## 🧪 Running Tests

```bash
pytest
```

Tests include:

- Weather API fetch  
- Cache save/load  
- Cache expiry  
- Terminal input handling  

---

## 📦 Requirements

```
streamlit
requests
pytest
```

SQLite is built into Python — no install needed.

---

## 🧰 Technologies Used

- **Python 3.10+**
- **Streamlit**
- **Requests**
- **SQLite**
- **Pytest**
- **VS Code**

---

## 📝 Notes

- The project uses **Open‑Meteo**, a free, no‑signup weather API.  
- The launcher automatically deletes `weather.db` before starting the web UI.  
- The UI is intentionally minimal and fast — no animations, no heavy styling.

---

## 📄 License

MIT License (or whatever you choose).

---

