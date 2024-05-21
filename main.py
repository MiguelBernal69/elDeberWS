from bs4 import BeautifulSoup
import requests
import bs4


URL_BASE = "https://eldeber.com.bo/"

pedidoObtenido = requests.get(URL_BASE)
htmlObtenido = pedidoObtenido.text

soup = BeautifulSoup(htmlObtenido, 'html.parser')

print(type(soup))
# primerH2 = soup.find('h2') #busca el primer h2
# print(primerH2.text)


todosH2 = soup.find_all('h2') #busca todos los h2
# print(todosH2)


# soloUnoH2 = soup.find_all('h2', limit=1) #busca todos los h2
# print(soloUnoH2)

# for seccion in todosH2:
#     print(seccion.text)
#     print("\n")
# print(len(todosH2))

# for seccion in todosH2:  # permite la limpieza de los datos en este caso limpiar los vacios
#     print(seccion.get_text(strip=True))
#     print("\n")

divs = soup.find_all('div', class_='region region-col-1')
for div in divs:
    # print(div.get_text(strip=True))
    print(div.prettify())
    print("\n")

print(len(divs))