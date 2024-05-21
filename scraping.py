import requests

latitud = -34.6
longitud = -58.4

fecha = '1816-07-09'
respuesta_sunset= requests.get(f'https://api.sunrise-sunset.org/json?lat={latitud}&lng={longitud}&date={fecha}&formatted=0')

datos_sunset = respuesta_sunset.json()

print(datos_sunset.keys())
print(datos_sunset['results']['sunset'])

print(f'status: {datos_sunset["status"]}')

print(datos_sunset['results'])