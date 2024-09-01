#Ejercicio 1
n = int(input("Ingrese un numero: "))   







'''
ingr = int(input("Ingrese el valor de Xi: "))
suma = 0
cont = 0
while ingr != -1:
    suma += ingr
    cont += 1
    ingr = int(input("Ingrese el valor de Xi: "))
promedio = suma/cont
print("El promedio es: ", round(promedio,1))


#Ejercicio 2

ingr = input("Ingrese un numero: ")#string

mayor = -float("inf") #donde vamos a guardar el mayor
menor = float("inf") #donde vamos a guardar el menor


while ingr != "FIN":
    ingr2 = int(ingr)
    if ingr2 > mayor: #Aqui preguntamos si es mayor
        mayor = ingr2#Aqui actualizamos el mayor
        
    if ingr2 < menor: #Aqui preguntamos si es menor
        menor = ingr2#Aqui actualizamos el menor
    ingr = input("Ingrese un numero: ")#string
print("El numero mayor es: ", mayor)
print("El numero menor es: ", menor)
  

'''
#Ejercicio 3
producto = 1 #donde vamos a guardar el valor
num = int(input("Ingrese el numero a calcular: "))
while num != 1: #mientras el numero distinto de 1
    producto*= num #guardamos el valor de la mult.
    num-=1 #sumamos al numero original -1
print("El valor de "+str(5)+"! es:", producto)
    
#Ejercicio 4
n = int(input('n: '))
i = 0
suma = 0
while i < n:
    suma += ((-1)**i) / (2*i+1)
    i += 1
print(suma*4)


    
    
