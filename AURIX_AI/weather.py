"""
=========================================
        AURIX AI - Weather Module
=========================================
"""

import requests

from config import (
    WEATHER_API_KEY,
    WEATHER_BASE_URL,
)

def get_weather(command):
    """
    Fetch current weather information
    from OpenWeather API.
    """

    try:
        # -----------------------------------
        # Extract city name
        # -----------------------------------

        city = (
            command.lower()
            .replace("weather in", "")
            .replace("weather at", "")
            .replace("weather for", "")
            .strip()
            .title()
        )

        if not city:
            return "Please tell me a city name."

        # -----------------------------------
        # API Request
        # -----------------------------------

        url = (
            f"{WEATHER_BASE_URL}"
            f"?q={city}"
            f"&appid={WEATHER_API_KEY}"
            "&units=metric"
        )

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return "Unable to connect to the weather service."

        data = response.json()

        # -----------------------------------
        # Check API Response
        # -----------------------------------

        if str(data.get("cod")) != "200":
            return f"Sorry, I couldn't find weather information for {city}."

        # -----------------------------------
        # Extract Data
        # -----------------------------------

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        # -----------------------------------
        # Build Response
        # -----------------------------------

        return (
            f"Weather in {city}: "
            f"{temperature}°C, "
            f"{description}. "
            f"Feels like {feels_like}°C, "
            f"Humidity {humidity}%, "
            f"Wind Speed {wind_speed} m/s."
        )

    except requests.exceptions.Timeout:
        return "Weather request timed out."

    except requests.exceptions.ConnectionError:
        return "No internet connection."

    except Exception as e:
        print(e)
        return "Weather service error."