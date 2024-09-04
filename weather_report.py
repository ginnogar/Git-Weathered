import requests
import argparse

api_key = "d3e70d5e32b4d965bf35a75ae7faa919"

parser = argparse.ArgumentParser(description="Obtener el clima para una ubicación específica.")
parser.add_argument("--location", type=str, required=True, help="Nombre de la ciudad y país (por ejemplo, 'Lima')")
parser.add_argument("--format", type=str, choices=["json", "csv", "text"], default="text", help="Formato de salida (json, csv, text)")

args = parser.parse_args()

locationn = args.location
format = args.format
url = f"http://api.openweathermap.org/data/2.5/weather?q={locationn}&appid={api_key}&units=metric" 

data = requests.get(url)
weather_data = data.json()
if weather_data:
    if format == "json":
        print(weather_data.json())
    elif format == "text":
        print(f"El clima en {locationn}: {weather_data['weather'][0]['description']}, {weather_data['main']['temp']}°C")
    
else:
    print("No se pudo obtener el clima. Verifica la ubicación o tu conexión.")
