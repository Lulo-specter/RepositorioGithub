"""
instalar pip install requests
instalar pip install beautifulsoup4
"""
import requests
from bs4 import BeautifulSoup
# Descargar la página web
url = 'https://incade.edu.ar/'
response = requests.get(url)

# Crear un objeto BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extraer información específica, como el pie de pagina <footer>
titulos = soup.find_all('footer')

# Mostrar los títulos
for titulo in titulos:
    print(titulo.text)