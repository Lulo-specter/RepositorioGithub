#Ejercicio N°3


### Código para Validar Fecha de Nacimiento


# Solicitar la fecha de nacimiento al usuario
fecha_nacimiento = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")

# Dividir la cadena en partes
partes = fecha_nacimiento.split("/")

# Verificar si se obtuvieron 3 partes
if len(partes) != 3:
    print("Formato inválido de fecha.")
else:
    # Desempaquetar las partes
    dia, mes, anio = partes

    # Validar que cada parte sea un string numérico
    if dia.isnumeric() and mes.isnumeric() and anio.isnumeric():
        dia = int(dia)
        mes = int(mes)
        anio = int(anio)

        # Realizar las validaciones
        if 1 <= dia <= 31 and 1 <= mes <= 12 and (len(str(anio)) == 4 and 1900 < anio < 2100):
            print("Fecha de nacimiento válida.")
        else:
            print("Fecha de nacimiento inválida.")
    else:
        print("Fecha de nacimiento inválida.")


### Explicación del Código
''''
1. **Entrada de Datos**:
   - Se solicita al usuario que ingrese su fecha de nacimiento en el formato "DD/MM/AAAA".

2. **División de la Cadena**:
   - La fecha ingresada se divide utilizando `split("/")`, que separa el día, el mes y el año.

3. **Verificación de Partes**:
   - Se comprueba si la longitud de la lista `partes` es igual a 3. Si no, se muestra un mensaje de formato inválido.

4. **Desempaquetado y Validación**:
   - Se desempaquetan las partes en `dia`, `mes` y `anio`.
   - Se verifica si cada parte es numérica usando `.isnumeric()`.
   - Se convierten a `int` para realizar las validaciones numéricas.
   - Se valida que:
     - El día esté en el rango de **1 a 31**.
     - El mes esté en el rango de **1 a 12**.
     - El año tenga **4 dígitos** y esté entre **1900 y 2100**.

5. **Resultado Final**:
   - Dependiendo de las validaciones, se muestra si la fecha es válida o inválida.

### Resultado Esperado

Este código permite al usuario ingresar su fecha de nacimiento y valida el formato y los valores ingresados, asegurando que sean correctos según las condiciones especificadas.

'''