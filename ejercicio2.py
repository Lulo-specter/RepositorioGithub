nota1 = int()
nota2 = int()
prom_notas = int()
progreso = str()
cond_final = str()
segundo_parc = str()

nota1 = int(input("Ingrese la nota del primer parcial: "))
nota2 = int(input("Ingrese la nota del segundo parcial: "))


prom_notas = ((nota1 + nota2)/2)
if (nota2 >= 7):
    segundo_parc = "Aprobado"
else:
    segundo_parc = "Desaprobado"

if (nota2 > nota1):
    progreso = "Mejoro su desempeño"
elif (nota2 == nota1):
    progreso = "Mantuvo la nota"
elif (nota2 < nota1):
    progreso = "Empeoro su desempeño "

if (prom_notas >= 7):
    cond_final = 'Promociono la Materia'
elif (prom_notas >= 4):
    cond_final = 'Debe Rendir Final'
else:
    cond_final = 'Recursa'

print("El promedio de notas es: ", prom_notas)
print(segundo_parc)
print("Progreso del 1er al 2do parcial: ", progreso)
print(cond_final)