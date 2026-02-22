import requests
from weather_cache import load_weather, save_weather

ICONS = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    61: "Rain",
    71: "Snow",
    95: "Thunderstorm"
}

def get_weather(city):
    # Try cache first
    cached = load_weather(city)
    if cached:
        return cached, True

    # Geocoding
    geo = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city, "count": 1}
    ).json()

    if "results" not in geo:
        return None, False

    lat = geo["results"][0]["latitude"]
    lon = geo["results"][0]["longitude"]

    # Weather + humidity
    weather = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": lat,
            "longitude": lon,
            "current_weather": True,
            "hourly": "relativehumidity_2m"
        }
    ).json()

    humidity = weather["hourly"]["relativehumidity_2m"][0]
    w = weather["current_weather"]

    data = {
        "city": geo["results"][0]["name"],
        "temp_c": w["temperature"],
        "temp_f": round(w["temperature"] * 9/5 + 32, 1),
        "wind": w["windspeed"],
        "humidity": humidity,
        "code": w["weathercode"],
        "time": w["time"]
    }

    save_weather(city, data)
    return data, False


def main():
    print("\n=== Weather Lookup (Terminal) ===")
    print("Data Source: Open‑Meteo (Live)\n")

    while True:
        city = input("Enter a city (or 'exit'): ").strip()
        if city.lower() == "exit":
            print("Goodbye.")
            break

        print("Loading weather…")

        weather, cached = get_weather(city)

        if not weather:
            print("City not found.\n")
            continue

        print(f"""
City: {weather['city']}
Temperature: {weather['temp_c']}°C / {weather['temp_f']}°F
Condition: {ICONS.get(weather['code'], 'Weather')}
Humidity: {weather['humidity']}%
Wind: {weather['wind']} m/s
Time: {weather['time']} UTC
Source: {"Cached" if cached else "Live API"}
""")


if __name__ == "__main__":
    main()
