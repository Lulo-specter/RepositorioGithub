print("\n-----------Venta de Zapallos-----------")

precio_por_kg = 1000
descuentos = {
    "dolares": 0.05,
    "yenes": 0.15,
    "guaranies": 0.20,
    "pesos": 0.10
}

comprador = input("Ingrese el nombre del comprador: ")
cant_zapallos = float(input("Ingrese la cantidad de zapallos (en kg): "))
tipo_de_moneda = input("Ingrese el tipo de moneda a pagar (dolares, yenes, guaranies, pesos): ").lower()

precio_tot_sin_desc = cant_zapallos * precio_por_kg
precio_tot_con_desc = 0

if tipo_de_moneda not in descuentos:
    nuevo_descuento = float(input(f"Ingrese el descuento para {tipo_de_moneda} (en decimal, ej: 0.15 para 15%): "))
   
    precio_por_kg *= 1.1
    descuentos[tipo_de_moneda] = nuevo_descuento
    print(f"Se ha agregado el descuento para {tipo_de_moneda} y se ha aplicado un recargo del 10% al precio.")


descuento = descuentos[tipo_de_moneda]
precio_tot_con_desc = precio_tot_sin_desc * (1 - descuento)


print("="*30)
print("RECIBO")
print("="*30)
print(f"Comprador: {comprador}")
print(f"Cantidad de zapallos: {cant_zapallos:.2f} kg")
print(f"Tipo de moneda: {tipo_de_moneda.title()}")
print(f"Descuento: {descuento * 100:.2f}%")
print(f"Precio sin descuento: ${precio_tot_sin_desc}")
print(f"Precio total: ${precio_tot_con_desc:.2f}")
print("="*30)