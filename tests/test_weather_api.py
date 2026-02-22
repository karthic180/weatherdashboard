import pytest
from web_app import get_weather

def test_valid_city_fetch():
    weather, cached = get_weather("Berlin")
    assert weather is not None
    assert "temp_c" in weather
    assert "humidity" in weather
    assert cached is False  # first fetch is live

def test_invalid_city():
    weather, cached = get_weather("zzzzzzzzzz")
    assert weather is None
