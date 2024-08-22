
#EJEMPLO 1
'''
numero = int(input("Ingrese un número: "))
if numero > 0 and numero % 2 == 0:
    print("El número es positivo y par")
'''
#EJEMPLO 2


edad = int(input("Ingrese una edad: "))
if edad < 12:
    print("Niño")
elif edad < 18:
    print("Adolescente")
elif edad < 65:
    print("Adulto")
else:
    print("Adulto Mayor")



#EJEMPLO 3

precio_base = 2500
peak = True  
edad = 30  
if edad < 5:
    mensaje = "Los niños menores de 5 años viajan gratis."
    precio_entrada = 0
elif edad <= 17:
    descuento = precio_base * 0.5
    precio_entrada = precio_base - descuento
    mensaje = "Los jóvenes de 5 a 17 años tienen un descuento del 50%. Precio de la entrada: $" + str(precio_entrada)
elif edad >= 65:
    mensaje = "Los adultos mayores de 65 años viajan gratis."
    precio_entrada = 0
else:
    precio_entrada = precio_base
    mensaje = "Los adultos de 18 a 64 años pagan tarifa completa. Precio de la entrada: $" + str(precio_entrada) 
if peak and precio_entrada != 0:
    recargo = precio_entrada* 0.2
    precio_final = precio_entrada + recargo
    mensaje += ". Aplicado un recargo del 20% por hora peak. Precio final: $" + str(precio_final)
print(mensaje)


#EJERCICIO FINAL


# Precio base por hora
precio_por_hora = 5.0
# Entradas del usuario
horas = float(input("Ingrese la cantidad de horas de servicio utilizadas: "))
hora_del_dia = int(input("Ingrese la hora del día en formato 24 horas (solo la hora): "))
codigo_promocional = input("Ingrese código promocional, si no tiene, déjelo en blanco: ")
# Cálculo del costo base
costo_base = horas * precio_por_hora
# Aplicación de descuentos por volumen de horas
if horas > 10 and horas < 20:
    descuento = 0.10  # 10%
elif horas >= 20:
    descuento = 0.20  # 20%
else:
    descuento = 0.0
costo_con_descuento = costo_base * (1 - descuento)
# Aplicación del recargo nocturno
if 18 <= hora_del_dia <= 23:
    recargo_nocturno = 0.15  # 15%
else:
    recargo_nocturno = 0.0
costo_con_recargos = costo_con_descuento * (1 + recargo_nocturno)
# Aplicación del código promocional
if codigo_promocional == "DESCUENTO20":
    descuento_promocional = 0.20  # 20%
else:
    descuento_promocional = 0.0
# Costo final
costo_final = costo_con_recargos * (1 - descuento_promocional)
# Mostrar el total a pagar
print("El total a pagar es: $ ", costo_final)

 
