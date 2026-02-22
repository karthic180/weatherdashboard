from weather_cache import save_weather, load_weather, clear_cache
from datetime import datetime, timedelta

def test_cache_save_and_load():
    data = {
        "city": "TestCity",
        "temp_c": 10,
        "temp_f": 50,
        "wind": 5,
        "humidity": 80,
        "code": 3,
        "time": datetime.utcnow().isoformat()
    }

    save_weather("TestCity", data)
    loaded = load_weather("TestCity")

    assert loaded is not None
    assert loaded["temp_c"] == 10
    assert loaded["humidity"] == 80

def test_cache_clear():
    clear_cache()
    assert load_weather("TestCity") is None
