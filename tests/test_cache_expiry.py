from weather_cache import save_weather, load_weather
from datetime import datetime, timedelta

def test_cache_expiry(monkeypatch):
    old_time = (datetime.utcnow() - timedelta(minutes=60)).isoformat()

    data = {
        "city": "OldCity",
        "temp_c": 10,
        "temp_f": 50,
        "wind": 5,
        "humidity": 80,
        "code": 3,
        "time": old_time
    }

    save_weather("OldCity", data)
    assert load_weather("OldCity") is None  # expired
