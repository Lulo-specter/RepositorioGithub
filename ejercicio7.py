# Cambios $$$ 
total_compra = float(input("Ingrese el total de la compra: "))
dinero_recibido = float(input("Ingrese el total del dinero recibido: "))
def calcular_cambio(total_compra, dinero_recibido):
    # Verificar si el dinero recibido es suficiente
    if dinero_recibido < total_compra:
        return "El dinero recibido es insuficiente."
    cambio = dinero_recibido - total_compra
    denominaciones = [500, 100, 50, 20, 10, 5, 1]
    cantidad_billetes = {}
    for billete in denominaciones:
        cantidad = cambio // billete
        if cantidad > 0:
            cantidad_billetes[billete] = cantidad
            cambio %= billete
    return cantidad_billetes
cambio = calcular_cambio(total_compra, dinero_recibido)
if isinstance(cambio, dict):
    print("Cambio a entregar:")
    for billete, cantidad in cambio.items():
        print(f"${billete}: {cantidad} billete(s)")
else:
    print(cambio)