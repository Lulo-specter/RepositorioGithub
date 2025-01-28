'''''
personajes= [
    "Harry Potter",
    "Hermione Granger",
    "Ron Weasley",
    "Albus Dumbledore",
    "Severus Snape",
    "Rubeus Hagrid",
    "Draco Malfoy",
    "Sirius Black",
    "Lord Voldemort",
    "Minerva McGonagall",
]

gryffindor = [
    "Harry Potter",
    "Hermione Granger",
    "Ron Weasley",
    "Albus Dumbledore",
    "Rubeus Hagrid",
    "Sirius Black",
    "Minerva McGonagall",
]

slytherin = ["Severus Snape",
              "Draco Malfoy", 
              "Lord Voldemort"]

personajes_ordenados = sorted(personajes)

print(f"Lista de personajes ordenados (Alfabeticamente): \n{personajes_ordenados} ")
print(f"\nTotal de personajes: {len(personajes_ordenados)}")

nombre_personaje = input("Ingrese el nombre del personaje: ")

if nombre_personaje in gryffindor:
    print(f"{nombre_personaje} pertenece a la casa Gryffindor: ")
elif nombre_personaje in slytherin:
    print(f"{nombre_personaje} pertenece a la casa Slytherin: ")
else:
    print("Personaje no encontrando en la casa Gryffindor o casa Slytherin.")
'''''