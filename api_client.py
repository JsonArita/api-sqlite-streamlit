import requests

API_URL = "https://jsonplaceholder.typicode.com/users"

def obtener_usuarios_api():
    """
    Obtiene la lista de usuarios desde la API.
    
    Returns:
        list: Lista de usuarios obtenida desde la API.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP 4xx/5xx
        return response.json()  # Devuelve la respuesta en formato JSON
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los usuarios: {e}")
        return []  # Devuelve una lista vacía en caso de error