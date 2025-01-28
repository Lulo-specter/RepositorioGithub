''''
Contexto:
Estás a cargo de la boletería de las Cataratas del Iguazú, en la provincia de Misiones, Argentina. 
Debés vender entradas a turistas nacionales y extranjeros, aplicando ciertos descuentos.

Reglas de negocio:

1.Entrada para extranjeros:  3000. 1.2.Entradaparaargentinos(nomisioneros): 1500.
2.Entrada para misioneros: $700.
3.Personas mayores de 60 años: aplicar un descuento del 25%.
Objetivo:
Desarrollar un programa que, repetidamente, solicite al usuario:

La nacionalidad ("arg" o "extr")
La provincia (solo si es argentino)
La edad
Luego muestre el precio a pagar.
El proceso debe repetirse mientras se desee seguir vendiendo entradas.

Condiciones a implementar:

Usar un bucle while para iterar la venta de múltiples tickets.
Emplear if-elif-else para determinar el precio final con base en expresiones booleanas.
Si se ingresa algún dato como "fin", el programa se detiene (break).
'''

nacionalidades = ["arg", "extr"]
precios = [3000, 1500, 700]
entrada = 0

seguir = input("Desea Ingresar si/no?\n>").upper() == "SI"

while seguir:
    dto = 1
    edad = input("Su edad?\n>")

    if edad == "fin":
        break

    if edad.isnumeric():
        edad = int(edad)
    else:
        print("Debe ingresar una edad numérica.")
        break

    if edad >= 60:
        dto = 0.75

    nacion = input("Ingrese 'arg'  si es Argentino o 'extr' sino lo es\n>")

    if nacion == "fin":
        break

    entrada = precios[0]
    while not nacion in nacionalidades:
        print("Ingrese una nacionalidad válida arg o extr por favor\n>")
        nacion = input("Es argentino arg o es extranjero extr?").lower()

        if nacion == "fin":
            break

    if nacion == "arg":
        entrada = precios[1]
        provincia = input("Provincia  de origen\n>").lower()

        if provincia == "fin":
            break

        if provincia == "misiones":
            entrada = precios[2]

    entrada = entrada * dto
    print(f"Deberá abonar: ${entrada:.2f}")
    seguir = input("Desea ingresar otro visitante si/no\n>").upper() == "SI"