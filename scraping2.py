import requests
from bs4 import BeautifulSoup

url="https://listado.mercadolibre.com.ar/ropa-accesorios/calzado/zapatillas/nuevo/zapatillas-basquet_PriceRange_90000-100000_AGE*GROUP_6725189_FILTRABLE*SIZE_12189539_NoIndex_True#applied_filter_id%3Dprice%26applied_filter_name%3DPrecio%26applied_filter_order%3D9%26applied_value_id%3D90000.0-100000.0%26applied_value_name%3D%2490.000+a+%24100.000%26applied_value_order%3D2%26applied_value_results%3D105%26is_custom%3Dfalse"

response= requests.get(url)

#vamos a ver si se conecto o no
if response.status_code==200:
     print("todo joya")
else:
     print("error codigo",response.status_code)

#vamos a obtener la informacion de la pagina
soup =BeautifulSoup(response.text, 'html.parser') #nos convierte la devolucioin en un texto

# #para saber que buscar hay que inspeccionar la pagina y encontrar la etiqueta que necesitamos
productos=soup.find_all('div', class_="poly-card__content")

print("obtuvimos ",len(productos)," productos") #miramos cuantos productos obtuvimos

for producto in productos:  #recorro la lista con un foreach
     titulo=producto.find('h2', class_="poly-box poly-component__title") #busco en cada elemento de la lista que tenga el titulo
     if titulo:
         print(titulo.text.strip()) #si tiene algun titulo que lo imprima el texto entre las etiquetas
    
     precio=producto.find('span', class_="andes-money-amount__fraction") #el precio esta en una etiqueta span y tiene la siguiente clase
     if precio:
         print("$",precio.text.strip())

"""""
investigar selenium
"""""
