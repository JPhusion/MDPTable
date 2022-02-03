import scrapers.weather as weather

weather_data = weather.call()
print(weather.descNow(weather_data))
