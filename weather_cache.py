import sqlite3
from datetime import datetime, timedelta
import os
DB_NAME = os.getenv("WEATHER_DB", "weather.db")

CACHE_EXPIRY_MINUTES = 30

def init_db():
    conn = sqlite3.connect("weather.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS cache (
            city TEXT PRIMARY KEY,
            temp_c REAL,
            temp_f REAL,
            wind REAL,
            humidity REAL,
            code INTEGER,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def load_weather(city):
    init_db()
    conn = sqlite3.connect("weather.db")
    c = conn.cursor()
    c.execute("SELECT * FROM cache WHERE city = ?", (city,))
    row = c.fetchone()
    conn.close()

    if not row:
        return None

    timestamp = datetime.fromisoformat(row[6])
    if datetime.utcnow() - timestamp > timedelta(minutes=CACHE_EXPIRY_MINUTES):
        return None

    return {
        "city": row[0],
        "temp_c": row[1],
        "temp_f": row[2],
        "wind": row[3],
        "humidity": row[4],
        "code": row[5],
        "time": row[6]
    }

def save_weather(city, data):
    init_db()
    conn = sqlite3.connect("weather.db")
    c = conn.cursor()
    c.execute("""
        INSERT OR REPLACE INTO cache
        (city, temp_c, temp_f, wind, humidity, code, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data["city"], data["temp_c"], data["temp_f"],
        data["wind"], data["humidity"], data["code"], data["time"]
    ))
    conn.commit()
    conn.close()

def clear_cache():
    init_db()
    conn = sqlite3.connect("weather.db")
    c = conn.cursor()
    c.execute("DELETE FROM cache")
    conn.commit()
    conn.close()
