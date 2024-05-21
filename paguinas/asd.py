# Importa las bibliotecas necesarias
from bs4 import BeautifulSoup
import requests
import csv

# URL base y parámetros de consulta para cargar más noticias
URL_BASE = "https://eldeber.com.bo/pais"
params = {"page": 5}  # Por ejemplo, si quieres cargar la página 2

# Lista para almacenar todas las noticias
todas_las_noticias = []

# Función para obtener noticias de una página
def obtener_noticias(url, parametros):
    response = requests.get(url, params=parametros)
    html = response.content.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div', class_=['region', 'jsx-742874305 component component--medium'])
    noticias = []
    for div in divs:
        # Procesa y extrae los datos de cada div de noticia
        # Agrega los datos a la lista de noticias
        noticias.append({
            "tipo_noticia": div.parent.find('h4').text.strip(),
            "descripcion": div.parent.find('h2').text.strip(),
            "tiempo": div.parent.find('span').text.strip(),
            "periodista": div.parent.find('a').text.strip(),
            "suscriptor": "Sí" if div.find('div', class_='jsx-2404121536 isPremium') else "No"
        })
    return noticias

# Obtener noticias de la página inicial
todas_las_noticias.extend(obtener_noticias(URL_BASE, params))

# Cargar más noticias si es necesario (repite este bloque según sea necesario)
# Por ejemplo, aquí cargamos la página 2
params["page"] = 5  # Cambia el número de página según sea necesario
todas_las_noticias.extend(obtener_noticias(URL_BASE, params))

# Imprime todas las noticias obtenidas
for noticia in todas_las_noticias:
    print(noticia)

print("Número total de noticias:", len(todas_las_noticias))
