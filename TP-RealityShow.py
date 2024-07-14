# Enunciado:

# De los 3 Jugadores de un Reality Show, se registra:
# nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibió en la etapa de votos
# Informar:
# a. nombre del candidato con más votos
# b. nombre y edad del candidato con menos votos
# c. el promedio de edades de los candidatos
# d. total de votos emitidos.
# Todos los datos se ingresan mediante input()

# Trabajo por Gabriel Alfonzo Comision 306

total_votos = 0
edad_total = 0

nombre1 = input("Ingrese el nombre del primer jugador: ")
edad1 = int(input("Ingrese la edad del primer jugador (mayor de 25): "))
while edad1 <= 25:
    print("La edad debe ser mayor a 25.")
    edad1 = int(input("Ingrese la edad del primer jugador (mayor de 25): "))
votos1 = int(input("Ingrese la cantidad de votos recibidos por el primer jugador (no menor a cero): "))
while votos1 < 0:
    print("La cantidad de votos no puede ser negativa.")
    votos1 = int(input("Ingrese la cantidad de votos recibidos por el primer jugador (no menor a cero): "))

total_votos += votos1
edad_total += edad1

nombre2 = input("Ingrese el nombre del segundo jugador: ")
edad2 = int(input("Ingrese la edad del segundo jugador (mayor de 25): "))
while edad2 <= 25:
    print("La edad debe ser mayor a 25.")
    edad2 = int(input("Ingrese la edad del segundo jugador (mayor de 25): "))
votos2 = int(input("Ingrese la cantidad de votos recibidos por el segundo jugador (no menor a cero): "))
while votos2 < 0:
    print("La cantidad de votos no puede ser negativa.")
    votos2 = int(input("Ingrese la cantidad de votos recibidos por el segundo jugador (no menor a cero): "))

total_votos += votos2
edad_total += edad2

nombre3 = input("Ingrese el nombre del tercer jugador: ")
edad3 = int(input("Ingrese la edad del tercer jugador (mayor de 25): "))
while edad3 <= 25:
    print("La edad debe ser mayor a 25.")
    edad3 = int(input("Ingrese la edad del tercer jugador (mayor de 25): "))
votos3 = int(input("Ingrese la cantidad de votos recibidos por el tercer jugador (no menor a cero): "))
while votos3 < 0:
    print("La cantidad de votos no puede ser negativa.")
    votos3 = int(input("Ingrese la cantidad de votos recibidos por el tercer jugador (no menor a cero): "))

total_votos += votos3
edad_total += edad3

promedio_edades = edad_total / 3

if votos1 >= votos2 and votos1 >= votos3:
    nombre_mas_votos = nombre1
    votos_mas_votos = votos1
else:
    if votos2 >= votos3:
        nombre_mas_votos = nombre2
        votos_mas_votos = votos2
    else:
        nombre_mas_votos = nombre3
        votos_mas_votos = votos3

if votos1 <= votos2 and votos1 <= votos3:
    nombre_menos_votos = nombre1
    edad_menos_votos = edad1
    votos_menos_votos = votos1
elif votos2 <= votos3:
    nombre_menos_votos = nombre2
    edad_menos_votos = edad2
    votos_menos_votos = votos2
else:
    nombre_menos_votos = nombre3
    edad_menos_votos = edad3
    votos_menos_votos = votos3

print(f"a. Nombre del candidato con más votos: {nombre_mas_votos} (Votos: {votos_mas_votos})")
print(f"b. Nombre y edad del candidato con menos votos: {nombre_menos_votos}, {edad_menos_votos} años (Votos: {votos_menos_votos})")
print(f"c. Promedio de edades de los candidatos: {promedio_edades}")
print(f"d. Total de votos emitidos: {total_votos}")
