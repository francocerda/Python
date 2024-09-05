# Solicitar mensaje al usuario
mensaje = input("Ingrese el mensaje a enviar por telégrafo: ")
costo_total = 0  # Inicializamos el costo total a 0

# Definimos los caracteres válidos
digitos = "0123456789"
letras_validas = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
caracteres_especiales = "ñáéíóúÑÁÉÍÓÚ"

# Recorremos cada carácter del mensaje
for caracter in mensaje:
    if caracter == " ":  # Si es un espacio, no tiene costo
        continue
    elif caracter in digitos:  # Si es un dígito
        costo_total += 20
    elif caracter in letras_validas:  # Si es una letra estándar
        costo_total += 10
    elif caracter in caracteres_especiales or (not caracter in letras_validas and not caracter in digitos and not caracter == " "):  # Caracteres especiales y otros no alfabéticos
        costo_total += 30
  
print("El costo total del mensaje es:", costo_total)
 

string_prueba = input("Ingrese un string: ")
contador = 0
inicio = 0
final = -1
for contador in range(len(string_prueba)):
    if(string_prueba[inicio] == string_prueba[final]):
        inicio += 1
        final -= 1
    else:
        print("No es palíndromo")
        break    
    contador += 1    
print("Es palíndromo") 



cadena = input("Ingrese cadena: ")
bases_validas = "ACGT"
grupos = cadena.split()
es_valida = True
for grupo in grupos:
    if len(grupo) != 4:
        es_valida = False
        break
    for caracter in grupo:
        if caracter not in bases_validas:
            es_valida = False
            break

    if not es_valida:
        break


if es_valida:
    print("Es valida")
else:
    print("No es valida")
    
