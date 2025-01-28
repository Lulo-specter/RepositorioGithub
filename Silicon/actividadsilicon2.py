#Ejercio, dias laborables 
dia = str()
print ("="*25)
dia = input ("Por favor, ingrese el dia de la semana: ").lower();
print ("="*25)
#Uso match para comparar el día ingresado (laborable o no)
match dia: 
    case "lunes" | "martes" | "miércoles" | "jueves" | "viernes":
        print ("="*15)
        print( "Es un día laborable.")
        print ("="*15)
    case "sabado" | "domingo":
        print ("="*15)
        print ("Fin de semana.")
        print ("="*15)
    case _:
        print ("="*15)
        print("Opción invalida.")
        print ("="*15)
print ("="*25)






'''''
# Solicitar al usuario que ingrese un día de la semana
dia = input("Por favor, ingresa un día de la semana en minúscula: ")

# Usar match para comprobar el día ingresado
match dia:
    case "lunes" | "martes" | "miércoles" | "jueves" | "viernes":
        print("Es un día laborable.")
    case "sábado" | "domingo":
        print("Es fin de semana.")
    case _:
        print("No parece ser un día válido.")
'''
