num = 10

decimal = 12.32131

suma = num + decimal


division = num % decimal
print(suma)
print(division)


numero = int(input("Dame una variable: "))

print(numero)


# Precio base por hora
precio_por_hora = 5.0
# Entradas del usuario
horas = int(input("Ingrese la cantidad de horas de servicio utilizadas: "))
hora_del_dia = int(input("Ingrese la hora del día en formato 24 horas (solo la hora): "))
codigo_promocional = input("Ingrese código promocional, si no tiene, déjelo en blanco: ")

costo_base = horas * precio_por_hora
# Aplicación de descuentos por volumen de horas
if horas > 10 and horas < 20:
    descuento = 0.10  # 10%
elif horas >= 20:
    descuento = 0.20  # 20%
else:
    descuento = 0.0





