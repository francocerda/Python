#EJERCICIO 1
# Definición de variables
numero_entero = 7
numero_real = 3.4

# Operaciones
suma = numero_entero + numero_real
resta = numero_entero - numero_real
multiplicacion = numero_entero * numero_real
division = numero_entero / numero_real
division_entera = numero_entero // numero_real
modulo = numero_entero % numero_real

# Imprimir resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División:", division_entera)
print("Módulo (residuo de la división):", modulo)


#EJERCICIO 2
# Solicitar entradas
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Calcular la suma
suma = numero1 + numero2

# Generar salida
print("La suma de", numero1, "y", numero2, "es", suma)



#EJERICIO 3
# Solicitar entrada
temperatura_fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))

# Conversión a Celsius
temperatura_celsius = (temperatura_fahrenheit - 32) * 5/9

# Generar salida
print(temperatura_fahrenheit, "grados Fahrenheit equivalen a", temperatura_celsius, "grados Celsius.")
