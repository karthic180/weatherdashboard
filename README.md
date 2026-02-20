#  Weather App — ETL + Terminal UI + Web UI
---

#  Features at a Glance

-  **Global City Search** — look up weather anywhere in the world  
-  **Fuzzy Matching** — find cities even with partial or misspelled names  
-  **Smart Fallbacks** — uses database first, then live API if needed  
-  **Rich Terminal UI** — optional color tables, borders, and panels  
-  **Streamlit Web UI** — clean, interactive dashboard  
-  **ETL Pipeline** — fetches and stores real‑time weather data  
-  **Auto‑Create DB** — no setup needed; the app builds the DB for you  
---

#  Getting Started

##  Install dependencies

```bash
pip install -r requirements.txt
```

Optional enhancements:

```bash
pip install rich rapidfuzz
```

- `rich` → color UI  
- `rapidfuzz` → fuzzy search  

Both optional — the app still works without them.

---

#  Database Handling

###  Automatic database creation  
If `weather.db` is missing, the launcher will automatically run:

```bash
python init_db.py
```

This creates the correct table structure with no user action required.

###  Reset Database  
The launcher includes a safe option to:

- Delete `weather.db`  
- Recreate it cleanly  

Useful for testing or starting fresh.

---

#  Diagnostics Mode

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

#  Running the App

Use the launcher to choose your interface:

```bash
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

#  Terminal Viewer Features

The terminal UI (`terminal_app.py`) includes:

###  Global City Search  
Type **any** city name:

- `tokyo`
- `new york`
- `sydney`
- `cairo`

If the city isn’t in the database, the app fetches **live weather** using Open‑Meteo.

###  Fuzzy Search  
Even messy inputs work:

- `ldn` → London  
- `brln` → Berlin  
- `ams` → Amsterdam  

###  Weather Icons  
Weather conditions are displayed with emoji:

-  Clear sky  
-  Rain  
-  Snow  
-  Thunderstorm  

###  Rich UI (optional)  
If `rich` is installed:

- Color tables  
- Borders  
- Panels  

If not installed → plain fallback.

---

#  Web UI (Streamlit)

Launch manually:

```bash
python -m streamlit run web_app.py
```

Or choose **Web UI** from the launcher.

### Auto‑install Streamlit  
If Streamlit is missing, the launcher will offer to install it.

###  Features  
- Dropdown city selector  
- Weather display  
- Clean, simple interface  

---

#  ETL Pipeline

Run manually:

```bash
python main.py
```

Or choose **Run ETL Now** from the launcher.

The ETL:

- Fetches weather for predefined cities  
- Inserts data into `weather.db`  
- Updates existing entries  

---

#  Resetting the Project

To completely reset:

1. Choose **Reset Database** in the launcher  
2. Run **Run ETL Now**  
3. Launch Terminal or Web UI  

---

#  How to Download the Project


##  Download ZIP

1. Go to the repository page  
2. Click the green **Code** button  
3. Select **Download ZIP**  
4. Extract the ZIP file  
5. Open a terminal inside the extracted folder  


---

#  How to Run the App

Once downloaded or cloned:

###  Install dependencies

```bash
pip install -r requirements.txt
```

Optional (recommended):

```bash
pip install rich rapidfuzz
```

###  Launch the app

```bash
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

Choose an option and enjoy the app.

---

#  Manual Commands (Optional)

### Run Terminal UI:
```bash
python terminal_app.py
```

### Run Web UI:
```bash
python -m streamlit run web_app.py
```

### Run ETL:
```bash
python main.py
```

### Create database manually:
```bash
python init_db.py
```

---
