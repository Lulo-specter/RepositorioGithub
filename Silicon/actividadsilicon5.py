'''''
Consigna
Contexto:
Imaginá que estás desarrollando el módulo de registro de usuarios para una plataforma. 
Por la sensibilidad de la información, la plataforma exige que el usuario cree una contraseña segura, 
con los siguientes criterios:

Longitud: Al menos 8 caracteres.
Variedad de caracteres:
Mayúsculas (por lo menos una)
Minúsculas (por lo menos una)
Dígitos numéricos (por lo menos uno)
Símbolos (por lo menos uno)
Si la contraseña no cumple con alguno de esos criterios, se lo notifica y se vuelve a pedir una nueva contraseña.
Si en algún momento el usuario ingresa la palabra especial "CANCELAR" (en mayúsculas o minúsculas), se finaliza el proceso sin validarla.
Objetivo:
Crear un ciclo de validación de contraseñas que, en cada iteración, pida una contraseña y revise dichos requisitos. Solamente cuando la contraseña cumple todas las reglas, se da por finalizado el registro, mostrando un mensaje de éxito.

Tip: Las cadenas son iterables que un bucle for puede recorrer caracter a caracter.
'''
import string

simbolos = string.punctuation + " "
mayusculas = string.ascii_uppercase
minusculas = string.ascii_lowercase

tiene_simbolos = tiene_mayusculas = tiene_minisculas = False

while True:
    password = input("Ingrese una contraseña: ")

    if password.lower() == "cancelar":
        print("Cancelado")
        break

    if len(password) < 8:
        print("La contraseña debe tener al menos 8 caracteres")
        continue

    for char in password:
        if char in simbolos:
            tiene_simbolos = True
        if char in mayusculas:
            tiene_mayusculas = True
        if char in minusculas:
            tiene_minisculas = True

    if tiene_simbolos and tiene_mayusculas and tiene_minisculas:
        print("Contraseña segura")
        break
    else:
        print(
            "Contraseña insegura, debe conter al menos un simbolo, una mayuscula y una minuscula"
        )
        tiene_simbolos = tiene_mayusculas = tiene_minisculas = False