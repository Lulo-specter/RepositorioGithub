# Metodos de listas en py #

lista = ["lunes", "martes", "miercoles"]
print (lista)

#imprime el segundo elemento
print(lista[1])
#longitud de lista
print (len(lista))

#agregar elemento
lista.append ("jueves")
print(lista)

#inserta un elemento en la posicion indicada
lista.insert(0, "domingo")
print(lista)

#extiende las listas
lista2 = ["viernes", "sabado"]
#lista.extend(lista2) extends puede agregar tambien tuplas, diccionarios, etc
lista += lista2
print(lista)

#eliminar elemento
lista.remove("sabado")
print(lista)

#eliminar el indice indicado
lista.pop(2)
print(lista)
#eliminar el ultimo elemento
print(lista.pop())
print(lista)

#eliminar lista
lista.clear()
print(lista)
lista=[2,3]

del lista
print(lista)