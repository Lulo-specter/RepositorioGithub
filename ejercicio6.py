import calendar

def fecha_valida(day, month, year):
    if 1 <= month <= 12 and 1 <= day <= calendar.monthrange(year, month)[1]:
        return True
    else:
        return False

print("==============Validacion de Fecha==============")
print("A continuacion ingrese la fecha a comprar en formato dd/mm/aaaa")

day = int(input("dia: "))
month = int(input("mes: "))
year = int(input("año: "))

if year <= 0:
    print("El año debe ser positivo.")
    exit()

if fecha_valida(day, month, year):
    print(f"La fecha es válida.")
    print(f"La fecha es: {day:02d}/{month:02d}/{year}")
else:
    print("La fecha no es válida.")
