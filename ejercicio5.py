#declaramos una funcion llamada mayor_unico
def mayor_unico(a, b, c):
    mayor = a #declaramos una variable llamada mayor a la cual le asignamos el primer valor como mayor

    mayor = (b * (b > mayor)) + (mayor * (b <= mayor)) #utilizamos esta operacion la cual nos permite saber a traves de TRUE = 1, FALSE = 0 para comparar el valor de b con el de mayor 
    mayor = (c * (c > mayor)) + (mayor * (c <= mayor)) #utilizamos esta operacion la cual nos permite saber a traves de TRUE = 1, FALSE = 0 para comparar el valor de c con el de mayor
    #declaramos una variable llamada es_unico
    es_unico = (a < mayor) + (b < mayor) + (c < mayor) #utilizamos una operacion similar a la anterior, pero en este caso buscando como resulta un 2(el cual nos dice que existend dos numeros que no son mayores), !=2 (damos por entendido que no existe un numero mayor unico)
    return mayor * (es_unico == 2) - (es_unico != 2) 

a = 30
b = 5
c = 15

resultado = mayor_unico(a,b,c)

if resultado != -1: #si nuestro resultado es distinto de -1, sabemos que el numero obtenido de la funcion mayor_unico, almacenado en la variable resultado, es un mayor unico
    print(f"El mayor unico es: {resultado}")
else: #de lo contrario, sabemos que no existe un mayor unico
    print("No existe mayor unico")


