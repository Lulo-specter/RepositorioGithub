
# Ejercicio No. 2, calificación de estudiantes
# Variables
nombre_completo = str()
calificacion = float()  # Para permitir decimales
beca = str()
# Información del estudiante
nombre_completo = input("Ingrese su nombre completo: ").title()
calificacion = float(input("Ingrese su calificación: "))
beca = input("¿Tiene una beca (SÍ/NO): ").lower()
tiene_beca = beca == "si"
# Determinar la condición del estudiante
if calificacion >= 7:
    condición = "Aprobado"
elif 4 < calificacion < 7:
    condición = "Regular"
else:
    condición = "Reprobado"
# Mensaje adicional
mensaje_beca = ""
if tiene_beca:
    mensaje_beca = "Tenés beneficios extra por tu beca."
else:
    mensaje_beca = "No tenes beneficios."
# Mostrar el resultado final
print("\nResumen del Estudiante")
print("="*50)
print(f"Nombre completo: {nombre_completo}")
print(f"Calificación: {calificacion}")
print(f"Beca: {beca}")
print(f"Condición: {condición}")
if mensaje_beca:
    print(mensaje_beca)
print("="*50)
