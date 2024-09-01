for i in range(5):
    palabra = input()
    if(i == 4):
        print("FLDSMDFR bloqueada!")
    elif( palabra == "FLDSMDFR21"):
        n = int(input())#Pedir Numero 
        n = n//3 #cantidad de hambuergesas que puede generar mi maquina
        asteriscos = "* "
        for i in range(n):
            print(asteriscos*(i+1))
        break  