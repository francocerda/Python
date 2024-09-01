edad_mayor = -float("inf")  # Inicializamos con el valor más bajo posible
nom_mayor = ""  # Inicializamos el nombre de la persona mayor como una cadena vacía
nombre = input("Nombre: ")  # Pedimos el nombre de la primera persona
edad = int(input("Edad: "))  # Pedimos la edad de la primera persona

while nombre != "FIN":  # Mientras el nombre no sea "FIN"
    if edad > edad_mayor:  # Si la edad actual es mayor que la edad mayor registrada
        edad_mayor = edad  # Actualizamos la edad mayor
        nom_mayor = nombre  # Actualizamos el nombre de la persona mayor
    nombre = input("Nombre: ")  # Pedimos el nombre de la siguiente persona
    if nombre != "FIN":  # Si el nombre no es "FIN"
        edad = int(input("Edad: "))  # Pedimos la edad de la siguiente persona

print("La persona mayor es", nom_mayor, "con", edad_mayor, "años")  # Mostramos quién es la persona mayor
