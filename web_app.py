import streamlit as st
import requests
from weather_cache import load_weather, save_weather, clear_cache

st.set_page_config(page_title="Weather Dashboard", layout="centered")

# Hide Streamlit chrome
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<div style='text-align:center; color:gray;'>Data Source: Open‑Meteo (Live)</div>",
    unsafe_allow_html=True
)

ICONS = {
    0: "☀️ Clear sky",
    1: "🌤 Mainly clear",
    2: "⛅ Partly cloudy",
    3: "☁️ Overcast",
    61: "🌧 Rain",
    71: "❄️ Snow",
    95: "⛈ Thunderstorm"
}

def get_weather(city):
    cached = load_weather(city)
    if cached:
        return cached, True

    geo = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city, "count": 1}
    ).json()

    if "results" not in geo:
        return None, False

    lat = geo["results"][0]["latitude"]
    lon = geo["results"][0]["longitude"]

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

st.markdown("<h2 style='text-align:center;'>🌦 Weather Lookup</h2>", unsafe_allow_html=True)

if st.button("Clear Cache"):
    clear_cache()
    st.success("Cache cleared.")

with st.form("search_form"):
    city = st.text_input("City:", placeholder="e.g., Berlin")
    submitted = st.form_submit_button("Search")

if submitted:
    if not city.strip():
        st.error("Please enter a city.")
    else:
        weather, cached = get_weather(city)
        if not weather:
            st.error("City not found.")
        else:
            st.markdown(
                f"""
                <div style="
                    background:#f8f9fa;
                    padding:20px;
                    border-radius:10px;
                    border:1px solid #ddd;
                    max-width:450px;
                    margin:auto;
                    font-size:18px;
                ">
                    <b>📍 City:</b> {weather['city']}<br>
                    <b>🌡 Temperature:</b> {weather['temp_c']}°C / {weather['temp_f']}°F<br>
                    <b>🌦 Condition:</b> {ICONS.get(weather['code'], 'Weather')}<br>
                    <b>💧 Humidity:</b> {weather['humidity']}%<br>
                    <b>💨 Wind:</b> {weather['wind']} m/s<br>
                    <b>🕒 Time:</b> {weather['time']} UTC<br>
                    <b>💾 Source:</b> {"Cached" if cached else "Live API"}
                </div>
                """,
                unsafe_allow_html=True
            )
