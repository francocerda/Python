'''
lista = list(range(1,12))
print(lista)# Crear la lista
lista = list(range(1, 11))


# 1. Agregar el número 11
lista.append(11)
print("Después de agregar 11:", lista)

# 2. Eliminar el número 5
lista.remove(5)
print("Después de eliminar 5:", lista)

# 3. Encontrar la posición del número 7
posicion_7 = lista.index(7)
print("Posición del número 7:", posicion_7)

# 4. Reversa el orden de la lista
lista.reverse()
print("Lista en orden inverso:", lista)

# 5. Ordenar la lista
lista.sort()
print("Lista ordenada:", lista)


print("\n\n")

def filtrar_impares(lista):
    impares = []
    for i in lista:
        if i%2 != 0:
            impares.append(i)
    impares.sort()
    impares.reverse()
    return impares

# Ejemplo de uso
lista = [10, 15, 20, 25, 30, 35, 40, 45]
nueva_lista = filtrar_impares(lista)
print("Lista original:", lista)
print("Lista de impares ordenada de mayor a menor:", nueva_lista)


'''










resultados = [ ["Huracan",160], ["918 Spyder",150], ["Roadster",220],
	["M5",45], ["Artura",10], ["720S",99],["911 Turbo S",100],
	["Urus",45], ["Nevera",130], ["M4 Competition",52],
	["SF90 Stradale",75], ["F8 Tributo",80]
]

modelos = [ ["Huracan",["Lamborghini","Gasolina",5.2,630,2.8]],
	["Urus",["Lamborghini","Gasolina",4,626,3.5]],
	["918 Spyder",["Porsche","Gasolina",4.6,887,2.2]],
	["911 Turbo S",["Porsche","Gasolina",3.8,640,2.6]],
	["Taycan",["Porsche","Eléctrico",0,616,2.6]],
	["SF90 Stradale",["Ferrari","Gasolina",4,986,2.5]],
	["F8 Tributo",["Ferrari","Gasolina",3.9,710,2.8]],
	["Roadster",["Tesla","Eléctrico",0,1000,1.9]],
	["570S",["McLaren","Gasolina",3.8,562,2.8]],
	["720S",["McLaren","Gasolina",4,568,2.7]],
	["Artura",["McLaren","Gasolina",3,531,3]],
	["M4 Competition",["BMW","Gasolina",3,503,3.9]],
	["Nevera",["Rimac","Eléctrico",0,1914,1.85]],
	["M5",["BMW","Gasolina",4.4,553,3.2]]
]

# Función #1
def mas_votados(votaciones, modelos):
    for modelo, votos in votaciones:
        print(modelo, votos)
	# Escriba aquí el código de la primera función

# Llamado de prueba para la función mas_votados()
print(mas_votados(resultados, modelos))

'''
# Función #2
def recomendar(votaciones, modelos, tipo_motor, cilindrada, potencia):
	# Escriba aquí el código de la segunda función

# Llamados de prueba para la función recomendar()

print(recomendar(resultados, modelos, "Eléctrico", 0, 500))
print(recomendar(resultados, modelos, "Eléctrico",0, 1000))
print(recomendar(resultados, modelos, "Gasolina", 3, 500))
print(recomendar(resultados, modelos, "Gasolina", 4, 1000))
'''




lista_de_listas = [[2, 2, 3], [1, 5, 6], [4, 8, 9]]



lista_de_listas.sort()
print(lista_de_listas)





