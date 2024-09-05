

'''
s1 = 'Este es un string con comillas simples.'
s2 = "Este es un string con comillas dobles."
s3 = "Aquí 'podemos' incluir comillas simples sin problemas."
s4 = 'Y aquí "podemos" hacer lo mismo con comillas dobles.'


palabra = "Python"
primera_letra = palabra[0]  # 'P'
ultima_letra = palabra[-1]  # 'n'


texto = "Hola mundo"
substr = texto[1:4]  # 'ola'
inicio = texto[:5]  # 'Hola '
fin = texto[5:]  # 'mundo'



saludo = "Hola"
# saludo[0] = "h"  # Esto es ilegal
saludo_nuevoo = "h" + saludo[1:]#Crea un nuevo string 'hola'.


a = "Hola"
b = "Mundo"
concatenado = a + " " + b  # 'Hola Mundo'
repetido = a * 2  # 'HolaHola'
longitud = len(a)  # 4
contiene = "a" in a  # True

'a' < 'b'  # True, porque 97 < 98 en ASCII.
'Ana' < 'ana'  # True, mayúsculas tienen un ASCII menor.


saludo = "Hola Mundo"
mayusculas = saludo.upper()  # 'HOLA MUNDO'
minusculas = saludo.lower()  # 'hola mundo'



texto = "Python"
for caracter in texto:
    print(caracter)

texto = "Python"
i = 0
while i < len(texto):
    print(texto[i])
    i += 1

'''
'''
# Definir el mensaje
mensaje = input("Ingrese su mensaje: ")

# Inicializar el costo total del mensaje
costo_total = 0

# Cadena de letras mayúsculas y minúsculas para comprobar si es una letra
letras_minusculas = 'abcdefghijklmnopqrstuvwxyzñáéíóú'
letras_mayusculas = letras_minusculas.upper()

# Cadena de dígitos
digitos = '0123456789'

# Iterar sobre cada carácter en el mensaje para calcular el costo
for caracter in mensaje:
    # Convertir el carácter a su versión en mayúscula y minúscula
    caracter_minuscula = caracter.lower()
    caracter_mayuscula = caracter.upper()

    # Verificar si el carácter es una letra
    if caracter_minuscula in letras_minusculas or caracter_mayuscula in letras_mayusculas:
        if caracter_minuscula in 'ñáéíóú':
            costo_total += 30  # Costo para caracteres especiales
        else:
            costo_total += 10  # Costo para letras normales
    # Verificar si el carácter es un dígito
    elif caracter in digitos:
        costo_total += 20
    # Verificar si el carácter es un carácter especial o un espacio
    elif caracter != ' ':
        costo_total += 30

# Imprimir el costo total del mensaje
print("El costo total del mensaje es: $" + str(costo_total))

'''



'''

# Solicitar la oración al usuario
texto_ingresado = input('Ingrese oracion: ')
texto_ingresado = texto_ingresado.lower()

# Eliminar espacios y comas del texto
texto_limpio = ''
contador = 0
while contador < len(texto_ingresado):
    if texto_ingresado[contador] != ' ' and texto_ingresado[contador] != ',':
        texto_limpio += texto_ingresado[contador]
    contador += 1

#print(texto_limpio)

# Construir el texto inverso
texto_inverso = ''
contador_inverso = len(texto_limpio) - 1
while contador_inverso >= 0:
    texto_inverso += texto_limpio[contador_inverso]
    contador_inverso -= 1

# Comparar el texto limpio con el texto inverso
if texto_limpio == texto_inverso:
    print(True)
else:
    print(False)

'''


cadena = input("Ingrese cadena: ")
# Agregamos un espacio al final para que pueda verificar
# la última sección
cadena = cadena + " "
bases = "AGCT"
i = 0
cant = 0
valida = True # Variable para determinar si es valida o no
while i < len(cadena):
    # Contamos las bases que van apareciendo
    if cadena[i] in bases:
        cant += 1
    # Si llegamos a un espacio verificamos que estén
    # de a cuatro    
    elif cadena[i] == " ":
        if cant != 4:
            valida = False
        cant = 0
    # Si no es un caso anterior, significa que es otra letra
    else:
        valida = False
    i+=1

if valida:
    print("Es valida")
else:
    print("No es valida")


