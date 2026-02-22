import os
import sqlite3
import pytest

TEST_DB = "test_weather.db"

@pytest.fixture(autouse=True)
def temp_db(monkeypatch):
    # Force weather_cache.py to use a test DB
    monkeypatch.setenv("WEATHER_DB", TEST_DB)

    # Remove old test DB
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

    yield

    # Cleanup after tests
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
