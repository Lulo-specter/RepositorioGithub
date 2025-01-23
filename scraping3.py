import requests
from bs4 import BeautifulSoup

# Descargar la página web
url = 'https://dolarhoy.com/'
response = requests.get(url)

# Crear un objeto BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extraer información específica donde marco las etiquetas que me interesan ej <div>
monedas = soup.find_all('div', class_='tile is-child')

"""
busco dentro de la etiqueta descargada anteriormente la informacion que necesito
utilizando los criterios de busqueda y comparacion
 """
for moneda in monedas:
    nombre=moneda.find('div', class_='title') #etiqueta div q tenga la clase title
    compra=moneda.find('div', class_=['compra', 'val']) #etiqueta div clases compra y val
    venta=moneda.find('div', class_=['venta', 'val'])
    if nombre:
        print (nombre.text.strip(), compra.text.strip()+" - "+ venta.text.strip())

