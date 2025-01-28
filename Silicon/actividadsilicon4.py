'''''
Consigna
Contexto:
En la localidad de San Ignacio, Misiones, hay un complejo de cabañas que se reservan dependiendo de la época del año y la cantidad de noches. Querés simular un sistema de reserva que:

Reciba mes de la reserva (ej. "enero", "julio", "septiembre") para distinguir temporada alta, media o baja.
Reciba cantidad de noches que la persona desea alojarse.
Según la combinación de mes y cantidad de noches, determina el precio total.
Reglas de negocio (valores a modo de ejemplo):

Temporada alta: diciembre, enero, febrero →  5000pornoche.−∗∗Temporadamedia∗∗:julio,agosto→ 4000 por noche.
Temporada baja: resto de los meses → $3000 por noche.
Descuento: si la cantidad de noches es mayor o igual a 7, se hace un 10% de descuento sobre el total, sin importar la temporada.
Objetivo:
Desarrollar un programa que:

Funcione en un bucle while pidiendo mes y cantidad de noches.
Use if-elif-else para determinar el precio por noche según la temporada.
Termine cuando el usuario no ingrese un dato (verificar con una expresión Falsy/Truthy).
'''

precio_base = 0

while True:
    mes = input("Ingrese el mes de la reserva (ej. enero, julio, septiembre): ").lower()

    # bool("") -> False
    if bool(mes) == False:
        break

    match mes:
        case "diciembre" | "enero" | "febrero":
            precio_base = 5000
        case "julio" | "agosto":
            precio_base = 4000
        case (
            "marzo"
            | "abril"
            | "mayo"
            | "junio"
            | "septiembre"
            | "octubre"
            | "noviembre"
        ):
            precio_base = 3000
        case _:
            print("No parece ser un mes válido")
            continue

    cantidad_noches = int(input("Ingrese la cantidad de noches a quedarse: "))

    if cantidad_noches >= 7:
        total = precio_base * cantidad_noches
        total = total - (total * 0.1)
        print(f"Total a pagar: {total} pesos. Hasta luego!")
    elif 0 < cantidad_noches < 7:
        total = precio_base * cantidad_noches
        print(f"Total a pagar: {total} pesos. Hasta luego!")
    elif bool(cantidad_noches) == False:
        break
    else:
        print("Lo siento, número no válido")
        continue