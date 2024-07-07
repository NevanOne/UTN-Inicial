#Ejercicio A
precio1 = float(input("Ingrese el precio del primer producto: "))
precio2 = float(input("Ingrese el precio del segundo producto: "))
precio3 = float(input("Ingrese el precio del tercer producto: "))

suma_precios = precio1 + precio2 + precio3
print(f"La suma de los tres precios es: {suma_precios}")

#Ejercicio B
promedio_precios = suma_precios / 3
print(f"El promedio de los tres precios es: {promedio_precios}")

#Ejercicio C
iva = 0.21
precio_final = suma_precios * (1 + iva)
print(f"El precio final con IVA (21%) es: {precio_final}")
