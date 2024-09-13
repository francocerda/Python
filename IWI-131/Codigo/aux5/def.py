def ordenado(n):
    palabra = str(n)
    for i in range(len(n)-1):
        if palabra[i] > palabra[i+1]:
            return False
    return True    
       
