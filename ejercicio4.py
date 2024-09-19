# Aulas # 
count = int()
anio = int()
suma_notas = 0
cuota_diaria = 1250
print("-------------------Listado de Aulas-------------------")
for dia in range(1,7):
    if dia % 2 == 0:
        aula = "A-300"
        print(f"Dia: {dia}          Aula: {aula}" )
    else:
        aula = "A-315"
        print(f"Dia: {dia}          Aula: {aula}" )
print("========================================================")
print()
print("-------------------Carga de Edades-------------------")
while True:  
    count = 0  
    anio = int(input("Ingrese una edad mayor o igual a 18: "))  # Solicita la edad inicialmente
    while anio < 18:
        count += 1 
        if count >= 3:
            print("Intentos superados, intente más tarde")
            break  
        anio = int(input("Error! Ingrese una edad mayor o igual a 18: "))  
    
    if anio >= 18:  
        print("Edad aceptada.")
    continuar = input("¿Desea ingresar otra edad? (s/n): ").lower()
    if continuar != 's':  
        print("Programa finalizado.")
        break  
print()
print("-------------------Promedio de Notas-------------------")
for i in range(5):
    nota=float(input(f"Ingrese la nota {i+1}: "))
    suma_notas += nota
promedio_notas = suma_notas/5
print(f"El promedio de las notas es: {promedio_notas}")
print("========================================================")
print()
print("-------------------Costo del Comedor-------------------")
for dia in range(1, 7):
    costo = cuota_diaria * dia  
    print(f"Día: {dia}           Costo: ${costo}")  
print("========================================================")
print()