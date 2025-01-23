#Calculo de Costos
coste = float()
peso = float()
peso = float(input("Ingrese el peso del paquete a enviar: "))

if peso <= 2:
    coste = 250
elif 2 <= peso <= 5:
    coste = 300
elif 5 <= peso <= 10:
    coste = 450
else:
    coste = 600

#Impresion 
print("="*50)
print("========Coste Equipaje========")
print(f"Peso: {peso}")
print(f"Coste: {coste}")
print("="*50)