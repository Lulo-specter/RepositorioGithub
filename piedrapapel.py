#mensaje de inicio del juego
print('''
       Bienvenido al juego Piedra Papel o Tijera
      ''')

#Variables seleccion de jugadores si quieres ser el numero uno ingresa primero tu nombre de usuario, de lo contrario seras el segundo
nombre_jugador_1 = input('Jugador 1 Ingrese su nombre: ')
nombre_jugador_2 = input('Jugador 2 Ingrese su nombre: ')

#En esta seccion te dira cual de los jugadores eres, si el primero o segundo y en base a eso quien tira primero
if nombre_jugador_1:
    print("Eres el jugador numero 1 " + nombre_jugador_1)

if nombre_jugador_2:
    print("Eres el jugador numero 2 " + nombre_jugador_2)

#Aqui tienes una lista de las opciones del juego [Piedra, Papel o Tijera]
lanzamientos_jugador = ['piedra', 'papel', 'tijera']

#Logica pasa saber que lanza cada jugador
lanzamiento_jugador1 = input(nombre_jugador_1 + ', Elije lanzar entre PIEDRA, PAPEL O TIJERA: ')
lanzamiento_jugador2 = input(nombre_jugador_2 + ', Elije lanzar entre PIEDRA, PAPEL O TIJERA: ')

#Logica del primer jugador
if lanzamiento_jugador1 not in lanzamientos_jugador:
    print(nombre_jugador_1 + ', No es una eleccion valida, intentalo nuevamente')
    lanzamiento_jugador1 = input(nombre_jugador_1 + ', Prueba lanzar con PIEDRA, PAPEL o TIJERA: ')

#Logica del segundo jugador
if lanzamiento_jugador2 not in lanzamientos_jugador:
    print(nombre_jugador_2 + ', No es una eleccion valida, intentalo nuevamente')
    lanzamiento_jugador2 = input(nombre_jugador_2 + ', Prueba lanzar con PIEDRA, PAPEL o TIJERA: ')

#Logica del empate entre jugadores y saber quien gana o pierde
if lanzamiento_jugador1 == lanzamiento_jugador2:
    print('EMPATE')
elif(lanzamiento_jugador1 == 'piedra' and lanzamiento_jugador2 == 'tijera') or\
    (lanzamiento_jugador1 == 'papel' and lanzamiento_jugador2 == 'piedra') or\
    (lanzamiento_jugador1 == 'tijera' and lanzamiento_jugador2 == 'papel'):
    print('GANA', nombre_jugador_1)
else:
    print('GANA', nombre_jugador_2)