import os
import requests
from dotenv import load_dotenv



def load_environment_variables():
    """Carga las variables de entorno necesarias."""
    load_dotenv()
    return os.getenv("API_KEY_SEARCH_GOOGLE"), os.getenv("SEARCH_ENGINE_ID")



def build_search_query():
    """Construye la consulta de búsqueda."""
    return 'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'

def build_search_url(api_key, search_engine_id, query, page, lang):
    """Construye la URL para la API de Google Custom Search."""
    return (
        f"https://www.googleapis.com/customsearch/v1?key={api_key}"
        f"&cx={search_engine_id}&q={query}&start={page}&lr={lang}"

    )

def fetch_search_results(url):
    """Realiza la solicitud a la API y devuelve los resultados."""
    response = requests.get(url)
    response.raise_for_status()  # Lanza un error si la respuesta es un error
    return response.json().get('items', [])

def format_result(item):
    """Formatea un resultado individual para su visualización."""
    title = item.get('title', 'Sin título')
    link = item.get('link', 'Sin enlace')
    snippet = item.get('snippet', 'Sin resumen')
    return f"Title: {title}\nLink: {link}\nSnippet: {snippet}\n{'-' * 80}"

def display_results(results):
    """Muestra los resultados de la búsqueda."""
    if not results:
        print("No se encontraron resultados.")
    else:
        for item in results:
            print(format_result(item))

def main():
    """Función principal que ejecuta el flujo del programa."""
    api_key, search_engine_id = load_environment_variables()
    query = build_search_query()
    page = 1
    lang = "lang_es"
    url = build_search_url(api_key, search_engine_id, query, page, lang)
    results = fetch_search_results(url)
    display_results(results)

if __name__ == "__main__":
    main()
    
    
    
   