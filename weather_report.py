import argparse # Librería para manejar argumentos desde la línea de comandos (CLI)
import requests # Librería para interactuar con APIs a través de solicitudes HTTP
from api_key import API_KEY  # Importa tu clave API desde un archivo externo

# Función que consulta el clima de una ubicación específica utilizando la API de OpenWeatherMap
def get_weather(location, api_key):
    # URL de la API con la ubicación y la clave API, especificando que queremos las unidades en grados Celsius (metric)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url) # Hace una solicitud GET a la API
    # Si la solicitud es exitosa (código 200), retorna los datos en formato JSON
    if response.status_code == 200:
        return response.json()
    else:
        return None # Si hay un error en la solicitud (cualquier código diferente de 200), retorna None

# Función principal del programa
def main():
    # Inicializamos el parser para gestionar los argumentos de la CLI
    parser = argparse.ArgumentParser(description="Obtener el clima para una ubicación específica.")
    
    # Agrega el argumento 'location' que es obligatorio (nombre de la ciudad y país)
    parser.add_argument("--location", type=str, required=True, help="Nombre de la ciudad y país (por ejemplo, 'Lima')")
    
    # Agrega el argumento 'format' que es opcional y permite elegir el formato de salida: json, csv o text
    parser.add_argument("--format", type=str, choices=["json", "csv", "text"], default="text", help="Formato de salida (json, csv, text)")
    
    # Parseamos los argumentos ingresados por el usuario
    args = parser.parse_args()

    # Asignamos la clave API
    api_key = API_KEY

    # Llamamos a la función get_weather con la ubicación proporcionada
    weather_data = get_weather(args.location, api_key)
    # Si los datos del clima fueron obtenidos exitosamente, mostramos la información
    if weather_data:
        # Si el formato seleccionado es JSON, imprimimos los datos crudos en formato JSON
        if args.format == "json":
            print(weather_data)
         # Si el formato seleccionado es texto (predeterminado), mostramos un resumen del clima
        elif args.format == "text":
            print(f"El clima en {args.location}: {weather_data['weather'][0]['description']}, {weather_data['main']['temp']}°C")
    else:
        # Si no se pudo obtener el clima, mostramos un mensaje de error
        print("No se pudo obtener el clima. Verifica la ubicación o tu conexión.")

# Este bloque asegura que la función main() se ejecute cuando se ejecute el script directamente
if __name__ == "__main__":
    main()
