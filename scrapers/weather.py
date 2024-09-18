"""
Note that data collected is from the OpenWeather API.
Documentation: https://openweathermap.org/api/one-call-api#data
"""

import requests

def call():
    lat, lon = -33.86500, 151.20944
    # API_key = "87a63db4499dfd7bc82e0bd0306f3240"
    API_key = "ce8c3c7d8000ca207b7e994530375e2e"
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,rain,showers,snowfall,weather_code&timeformat=unixtime&timezone=Australia%2FSydney&forecast_days=1")
    return response.json()

def tempNow(data):
    return data["current"]["temp"]

def feelsNow(data):
    return data["current"]["feels_like"]

def descNow(data):
    return data["current"]["weather"][0]["description"].capitalize()

def icon(data):
    return data["current"]["weather"][0]["icon"]

if __name__ == "__main__":
    data = call()
    print(data)
