'''
lista = list()

otra_lista = list([2,"Hola Mundo",False])

lista_nombres = list(["Susana","Natalia","Jesus","Seba"])
print(lista_nombres[-1])
print(lista_nombres[0])
print(lista_nombres[1])
print(lista_nombres[-2])


print("-----------------------------")

for var in lista_nombres:
    print(var)

edades = [20, 41, 6, 18, 23]

for i in range(len(edades)):
    print(edades[i])

indice = 0

while indice < len(edades):
    print(edades[indice])
    indice += 1

'''
numeros = []

numeros.append(10)
numeros.append(421)
numeros.append(-2)

for i in range(len(numeros)):
    print(numeros[i])

print(numeros)

otros_numeros = numeros

print(otros_numeros)