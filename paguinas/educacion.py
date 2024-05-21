from bs4 import BeautifulSoup
import requests
import csv

URL_BASE = "https://eldeber.com.bo/educacion-y-sociedad"

pedidoObtenido = requests.get(URL_BASE)
htmlObtenido = pedidoObtenido.content.decode('utf-8')

soup = BeautifulSoup(htmlObtenido, 'html.parser')

divs = soup.find_all('div', class_=['region', 'jsx-742874305 component component--medium'])

tipos_noticia = []
descripciones = []
tiempos = []
periodistas = []
suscriptores = []

for div in divs:
    tipo_noticia_elem = div.parent.find('h4')
    descripcion_elem = div.parent.find('h2')
    tiempo_elem = div.parent.find('span')
    periodista_elem = div.parent.find('a')
    suscriptor_elem = div.find('div', class_='jsx-2404121536 isPremium')  # Elemento que indica si es exclusivo para suscriptores
    
    # Verificar si los elementos existen antes de acceder a sus atributos
    if tipo_noticia_elem:
        tipo_noticia = tipo_noticia_elem.text.strip()
    else:
        tipo_noticia = "No encontrado"
    
    if descripcion_elem:
        descripcion = descripcion_elem.text.strip()
    else:
        descripcion = "No encontrada"
    
    if tiempo_elem:
        tiempo = tiempo_elem.text.strip()
    else:
        tiempo = "No encontrado"
    if periodista_elem:
        periodista = periodista_elem.text.strip()
    else:
        periodista = "No encontrado"
    
    # Verificar si la noticia es exclusiva para suscriptores
    if suscriptor_elem:
        suscriptor = "Sí"
    else:
        suscriptor = "No"
    
    tipos_noticia.append(tipo_noticia)
    descripciones.append(descripcion)
    tiempos.append(tiempo)
    periodistas.append(periodista)
    suscriptores.append(suscriptor)


for i in range(len(divs)):
    print("Tipo de noticia:", tipos_noticia[i])
    print("Descripción:", descripciones[i])
    print("Tiempo:", tiempos[i])
    print("Periodista:", periodistas[i])
    print("Exclusivo para suscriptores:", suscriptores[i])
    print()  # Salto de línea para separar las noticias

print("Número de divs encontrados:", len(divs))
print("Número de elementos en cada lista:", len(tipos_noticia), len(descripciones), len(tiempos), len(periodistas), len(suscriptores))

with open('datos_eldeber.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    # Escribe los nuevos datos en el archivo
    for i in range(len(divs)):
        if tiempos[i] != "No encontrado":
            writer.writerow(['educacion_sociedad',tipos_noticia[i], descripciones[i], tiempos[i], periodistas[i], suscriptores[i]])
