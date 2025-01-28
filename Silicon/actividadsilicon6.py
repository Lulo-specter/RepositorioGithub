#Ejercicios con listas
'''''
Actividad
frutas = ["manzana", "mango", "naranja", "kiwi", "arándano"]
print(frutas)
frutas2 = ["pera", "sandia", "uva", "durazno", "banana"]
print(frutas2)
frutas2.append("manzana")
print(frutas2)
frutas2.extend(frutas)
print(frutas2)
frutas.remove("kiwi")
print(frutas)
'''''
'''''
Ejemplo1
print("Ahora voy a ordenar mi lista")
frutas.sort()
# La ordenación se realiza EN la lista, es decir, se muta
print(f"La lista ordenada de frutas es: {frutas}")
print(f"El ID de la lista es: {id(frutas)}")
'''''



