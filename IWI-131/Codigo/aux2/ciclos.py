#Numeros de Amstrong
'''
n = int(input(""))
aux_n = n
suma = 0
tamanio = str(n)
n_digitos = len(tamanio)
for i in range(n_digitos):
    resto = n%10
    n = n//10
    suma = suma + (resto)**n_digitos
if suma == aux_n:
    print("Es de Armstrong")
else:
    print("No es de Armstrong")
'''

#La máquina de comida
'''
for i in range(5):
    palabra = input()
    if(i == 4):
        print("FLDSMDFR bloqueada!")
    elif( palabra == "FLDSMDFR21"):
        n = int(input())
        n = n//3
        asteriscos = "* "
        for i in range(n):
            print(asteriscos*(i+1))
        break    
'''
#Enrachao
'''
numero_anterior = None
repeticiones = 0
contador = 0
flag = True
while flag:
    n = int(input())
    contador +=1

    if numero_anterior == n:
        repeticiones +=1
    else:
        repeticiones = 1
        numero_anterior = n
    if n == repeticiones:
        print(contador)
        flag = False
'''  
#La fiesta de programadoras      
'''  
aforo = 5
contador = 0
while contador < aforo:
    nombre = input()
    if nombre == "Ada" or nombre == "Joan" or nombre == "Katherine" or nombre == "Alexandra" or nombre == "Barbarita":
        contador += 1
        print(contador, "Bienvenida", nombre, "!")
    else:
        print("Acceso denegado X")
        
print("Aforo completo")
'''  
#Ridiculus velosus (Recolección de semillas)
n = int(input())
dia_anterior = 1
dia_actual = 2
total_semillas = 3
dias = 2 
while total_semillas < n:
    siguiente = dia_anterior + dia_actual
    total_semillas += siguiente
    dia_anterior = dia_actual
    dia_actual = siguiente
    dias += 1
print(dias)   




    








    
