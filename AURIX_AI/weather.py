import requests
from config import WEATHER_API_KEY, WEATHER_BASE_URL


def get_weather(command):

    try:
        # clean input properly
        city = (
            command.lower()
            .replace("weather in", "")
            .replace("weather at", "")
            .strip()
        )

        if not city:
            return "Please tell me a city name."

        url = (
            f"{WEATHER_BASE_URL}"
            f"?q={city}"
            f"&appid={WEATHER_API_KEY}"
            "&units=metric"
        )

        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            return "City not found. Please try again."

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        return f"{city.title()} weather: {temp}°C with {desc}"

    except Exception:
        return "Weather service error"