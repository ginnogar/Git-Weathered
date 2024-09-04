import requests

location = "Asuncion"
api_key = "d3e70d5e32b4d965bf35a75ae7faa919"
format = "json"

url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric" 

weather_data = requests.get(url)
if weather_data:
    if format == "json":
        print(weather_data.json())
    elif format == "text":
        print(f"El clima en {location}: {weather_data['weather'][0]['description']}, {weather_data['main']['temp']}°C")
    # Puedes agregar la lógica para csv aquí
else:
    print("No se pudo obtener el clima. Verifica la ubicación o tu conexión.")
