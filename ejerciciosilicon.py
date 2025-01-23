# Variables

nombre = ""
cantidad_entradas = 0
precio = 500.5
descuento = ""
codigo_descuento = ""  # Inicializar la variable para el código de descuento
descuento_aplicado = 0  

print("=" * 50)
print("========== Bienvenido al Sistema de Reservas de entrada ==========")
print("=" * 50)

# Solicitar nombre al usuario
nombre = input("Ingrese su nombre: ") 

# Solicitar cantidad de entradas
cantidad_entradas = int(input("Ingrese la cantidad de entradas que desea reservar: "))

# Calcular el valor de las entradas
precio_entrada = cantidad_entradas * precio

# Preguntar si posee un código de descuento
descuento = input("Posee un código de descuento? (si/no): ")

if descuento.lower() == "si":
    codigo_descuento = input("Por favor ingrese el código: ")
    codigo_descuento = codigo_descuento.upper()  
    print(f"Código Ingresado: {codigo_descuento}")
else:
    print("No se ha registrado ningún código.")

# Verificar el código de descuento
if codigo_descuento == "SILICON2025":
    descuento_aplicado += (precio_entrada * 20) / 100  # Descuento del 20%

# Aplicar descuento adicional por cantidad de entradas
if cantidad_entradas >= 5:  
    descuento_aplicado += (precio_entrada * 10) / 100  # Descuento del 10%

# Calcular el precio final después de aplicar los descuentos
precio_final = precio_entrada - descuento_aplicado  # Resta del descuento aplicado

# Mostrar resultados
print("=" * 50)
print("=======Ticket=======")
print(f"Nombre: {nombre}")
print(f"Precio por entrada: {precio}")
print(f"Precio subtotal: {precio_entrada}")
print(f"Descuento Aplicado: {descuento_aplicado}")
print(f"Precio total: {precio_final}")
print("=" * 50)


'''
Si ingresa "SILICON2025", aplicarle un 20% de descuento al subtotal.
Si la cantidad de entradas supera 5, aplicarle un 10% de descuento al subtotal.
Mostrar al final:
El nombre,
El precio base,
El subtotal antes de descuentos,
El descuento total (si existe),
El total final.
'''
