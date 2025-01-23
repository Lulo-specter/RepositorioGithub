def es_palindromo(texto):
  """
  Determina si un texto es un palíndromo.

  Args:
    texto: El texto a evaluar.

  Returns:
    True si el texto es un palíndromo, False en caso contrario.
  """

  texto = texto.lower().replace(" ", "")  # Convertir a minúsculas y eliminar espacios
  texto_invertido = texto[::-1]  # Invertir el texto
  return texto == texto_invertido  # Comparar el texto original con el invertido

# Ejemplo de uso
texto1 = "casa"
texto2 = "Hola mundo"

if es_palindromo(texto1):
  print(f"{texto1} es un palíndromo.")
else:
  print(f"{texto1} no es un palíndromo.")

if es_palindromo(texto2):
  print(f"{texto2} es un palíndromo.")
else:
  print(f"{texto2} no es un palíndromo.")