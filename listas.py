# Listas en Python

mi_lista = list()
mi_otra_lista = []
print(len(mi_lista))

mi_lista = [21, 18, 35, 24, 62, 52, 30, 17,24]
print(len(mi_lista))

mi_otra_lista = [21, 1.67, "Luciano", "López", "Luciano"]
print(mi_otra_lista)

print(type(mi_otra_lista))
print(type(mi_lista))   


print(mi_otra_lista[0])
print(mi_otra_lista[1])
print(mi_otra_lista[-1])
print(mi_otra_lista[-4])
# print(mi_otra_lista[4]) IndexError
# print(mi_otra_lista[-5]) IndexError
print(mi_otra_lista.count("Luciano"))

print(mi_lista + mi_otra_lista)

mi_otra_lista.append("MercadoLibre")
print(mi_otra_lista)

mi_otra_lista.insert(1, "Verde")
print(mi_otra_lista)

mi_otra_lista[1] = ("Azul")
print(mi_otra_lista)

mi_otra_lista.remove("Azul")
print(mi_otra_lista)

print(mi_lista)

mi_lista.remove(24)
print(mi_lista)

mi_lista.pop()
print(mi_lista)

print(mi_lista.pop())
print(mi_lista)

element_pop = mi_lista.pop(2)
print("Elemento desapilado: ", element_pop)
print(mi_lista)

del mi_lista[2]
print(mi_lista)

mi_nueva_lista = mi_lista.copy()

mi_lista.clear()
print(mi_lista)
print(mi_nueva_lista)

mi_nueva_lista.reverse()
print(mi_nueva_lista)

mi_nueva_lista.sort()
print(mi_nueva_lista)

print(mi_nueva_lista[1:3])

mi_lista =  "Hola Python"
print(mi_lista)
print(type(mi_lista))