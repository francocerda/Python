string = input("Ingrese un string: ")
maximo = 0
contador = 0
precio_total = 100 
for caracter in string:
    if caracter == " ":
        precio_total += 100 
        if contador > maximo:
            maximo = contador  
        contador = 0  
    else:
        contador += 1 
if contador > maximo:
    maximo = contador
precio_total += maximo * 1.5  
print(int(precio_total))
