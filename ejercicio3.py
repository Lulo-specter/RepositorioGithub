# Ejercicio 3 #
aulas = int()
descuento = int()
estacionamiento = str()
turno = str()
cant_materias = int()
aula = str()
valor_cuota = 30000
valor_estacionamiento = int()
print("==================== AULAS ====================")
aulas = int(input("Ingrese el numero del dia: 1 (Lunes) a 6 (Sabado): "))
if (aulas % 2 == 0):
    aula = "A-300"
    print(aula)
else:
    aula = "A-315"
    print(aula)
print()
print("==================== Descuentos y Estacionamiento ====================")
turno = (input("Ingrese el turno: Mañana, Tarde o Noche: "))
cant_materias = int(input("Ingrese la cantidad de Materias: "))
print(f"Materias: {cant_materias}")
if (turno == "Tarde" and cant_materias >= 3):
    descuento = ((valor_cuota * 25) / 100)
    print("El valor de la cuota es: $",descuento)
else:
    descuento = ((valor_cuota * 5)/100)
    print(f"El valor de la cuota es: ${descuento}")
estacionamiento = input("Ingrese el vehiculo en el que ingresa: Auto, Moto o Bicicleta: ")
if(estacionamiento == "Auto" or estacionamiento == "Moto"):
    valor_estacionamiento = 300
    print(f"El costo de estacionamiento para Auto/Moto es: ${valor_estacionamiento}")
else:
    valor_estacionamiento = 50
    print(f"El costo de estacionamiento para Auto/Moto es: ${valor_estacionamiento}")
