from bs4 import BeautifulSoup
import requests

URL_BASE = "https://eldeber.com.bo/"

pedidoObtenido = requests.get(URL_BASE)
htmlObtenido = pedidoObtenido.text

soup = BeautifulSoup(htmlObtenido, 'html.parser')

divs = soup.find_all('div', class_='region region-col-1')
for div in divs:
    h4_element = div.parent.find('a')
    if h4_element:
        print(h4_element.text.strip())
    else:
        print("No se encontró ningún elemento h4 dentro del padre de este div")


print(len(divs))
