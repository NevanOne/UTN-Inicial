# Ejercicio 1
NombreDeUsuario = input('Ingrese su nombre de usuario: ')
print("Hola " + NombreDeUsuario)
# Ejercicio 2
Numero1 = int(input("Ingrese el primer numero: "))
Numero2 = int(input("Ingrese el segundo numero: "))
resultado = (Numero1 + Numero2)
print(resultado)
# Ejercicio 3
Nombre = input('Ingrese su Nombre: ')
Apellido = input('Ingrese su Apellido: ')
Edad = int(input('Ingrese su edad: '))
print(f"Nombre : {Nombre}, Apellido : {Apellido}, Edad: {Edad}")
# Ejercicio 4 
Nombre2 = input('Ingrese su Nombre: ')
NComision = int(input('Ingrese su Numero de Comision: '))
Asignatura = input('Ingrese la Asignatura: ')
Docente = input('Ingrese nombre del Docente Correspondiente: ')
Presente = bool(input('Usted estuvo presente ?:'))
print(f"Nombre : {Nombre2}, N°Comision : {NComision}, Asignatura: {Asignatura}, Docente: {Docente}, Estuvo presente? {Presente}")
# Ejercicio 5 
lado = float(input("Ingrese el lado del cuadrado: "))
superficie1 = lado ** 2
print(f"La superficie del cuadrado es: {superficie1}")
# Ejercicio 6
lado1 = float(input("Ingrese el primer lado del rectángulo: "))
lado2 = float(input("Ingrese el segundo lado del rectángulo: "))
superficie2 = lado1 * lado2
print(f"La superficie del rectángulo es: {superficie2}")
# Ejercicio 7
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
superficie3 = (base * altura) / 2
print(f"La superficie del triángulo es: {superficie3}")
#Ejercicio 8
nombre_producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
iva = precio * 0.21
precio_con_iva = precio + iva
print(f"Producto: {nombre_producto}, Precio: {precio}, Valor del IVA: 21%, Precio con IVA: {precio_con_iva}")
# Ejercicio 9
nombre_alumno = input("Ingrese el nombre del alumno: ")
apellido_alumno = input("Ingrese el apellido del alumno: ")
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
print(f"Alumno: {nombre_alumno} {apellido_alumno} , Notas: {nota1}, {nota2}, {nota3}, Promedio: {promedio}")
# Ejercicio 10
nombre_futuro = input("Ingrese su nombre: ")
edad_ej10 = int(input("Ingrese su edad: "))
edad_futura = edad_ej10 + 10
print(f"{nombre_futuro}, en 10 años tendrás {edad_futura} años.")