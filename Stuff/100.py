flag = True
suma = 0
while flag:
    opcion = int(input("Digite su numero: "))
    suma += opcion
    if suma >= 100:
        flag = False

print(suma)