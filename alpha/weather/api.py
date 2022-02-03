"""
Note that data collected is from the OpenWeather API.
Documentation: https://openweathermap.org/api/one-call-api#data
"""

import requests

def call():
    lat, lon = -33.86500, 151.20944
    API_key = "87a63db4499dfd7bc82e0bd0306f3240"
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&appid={API_key}")
    return response.json()

def gettempNow(data):
    return data["current"]["temp"]

def getfeelsNow(data):
    return data["current"]["feels_like"]

def getdescNow(data):
    return data["current"]["weather"][0]["description"]

def geticon(data):
    return data["current"]["weather"][0]["icon"]
