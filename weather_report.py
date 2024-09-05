import argparse #Libreria para crear CLI. 
import requests #Libreria que te permite interactuar con APIs
from api_key import API_KEY

def get_weather(location, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    parser = argparse.ArgumentParser(description="Obtener el clima para una ubicación específica.")
    parser.add_argument("--location", type=str, required=True, help="Nombre de la ciudad y país (por ejemplo, 'Lima')")
    parser.add_argument("--format", type=str, choices=["json", "csv", "text"], default="text", help="Formato de salida (json, csv, text)")
    
    args = parser.parse_args()

    api_key = API_KEY
    weather_data = get_weather(args.location, api_key)
    if weather_data:
        if args.format == "json":
            print(weather_data)
        elif args.format == "text":
            print(f"El clima en {args.location}: {weather_data['weather'][0]['description']}, {weather_data['main']['temp']}°C")
    else:
        print("No se pudo obtener el clima. Verifica la ubicación o tu conexión.")

if __name__ == "__main__":
    main()
