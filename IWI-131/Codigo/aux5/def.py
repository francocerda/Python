#RUTEO 1
a = 943
flag = True
n = 0
b = 0
c = 0
while flag :
    d = a % 10
    a = a // 10
    n = n * 10 + d
    if d % 2 == 0:
        b = b + 1
    else:
        c = c + 1
    if a == 0:
        flag = False
print (n,b,c)


#RUTEO 2
def f1(st):
    c=0
    h=len(st)
    s=0
    while c<h:
        if c!=h-1 and st[c+1]=='-':
            c+=2
        else:
            c+=3
        s+=1
    return s

n='1-5-13-18-19'
a = f1(n)
print(a)


#RUTEO 3

def b1(a):
    if a % 3 == 0:
        a = a + 3*a
    elif a**2 > 20:
        a = a + 2
    return str(a)

def b2(x, y):
    p = ''
    while x >= len(p):
        if x %2 != 0:
            p = p + b1(x)*2
            x = x - 2
    return int(p)%100
a = 5
b = 30475
print(b2(a, b))

#RUTEO 4

def f1(x):
    x = int(x)
    if x % 2 == 0:
        return True
    return False


def f2(b):
    i = 0
    while i < 10:
        if str(i) == b:
            return True
        i += 1
    return False

x = '1a2'
i = 0
p = 0
while i < len(x):
    if f2(x[i]):
        if f1(x[i]):
            p += 1
    i += 1
 
if p > len(x) / 2:
    print("Sirve")
else:
    print("No Sirve")



#RUTEO 5

def f1(c):
    if int(str(c)[0]) == 2:
        return int(c[0])
    elif int(c) > 10:
        c = int(c) / 10
    else:
        c = str(int(c) - 1)
    return c

def f2(b, c):
    b = b * c
    i = 0
    while len(b) >= i:
        i = f1(b)
        if i != 1:
            i = i + 1
        else:
            b = str((int(b) %2)+1)*2
    return b * i
a = '1'
b = 2
print f2(a, b) + str(f1(b + 2))


#RUTEO 6
def f1(a,b):
    if a!=b:
        i = 1
        while i<=b:
            j=0
            s=''
            while j<i:
                s = s+"*"
                j = j+1
            print s
            i = i+1
        return "#"*abs(a-b)
    else:
        return "#"*a
x=3
y=2
while y<=x:
    print f1(y,x)
    y = y+1


#PREGUNTA 1

total=0
disp=20
while disp>0:
    e_ninios=int(input('Ingrese entradas ninios: '))
    e_adultos=int(input('Ingrese entradas adultos: '))
    if e_ninios+e_adultos<=disp:
        boleto=e_ninios*1000+e_adultos*3000
        disp-=e_ninios+e_adultos
        total+=boleto
        print('Pague $'+str(boleto))
    else:
        print('No quedan boletos')
print('Hoy vendiste $',total)


#PREGUNTA 2

def ordenado(n):
    n = str(n)
    i = 0
    while i+1 < len(n):
        if n[i+1]>n[i]:
            return False 
        i+=1
    return True

def crear_password(numero):
    mayor = -float('inf')
    menor = float('inf')
    numero = str(numero)
    i = 0
    while i+1 < len(numero):
        doble = int(numero[i:i+2])
        if doble > mayor:
            mayor = doble 
        if doble < menor:
            menor = doble 
        i+=1 
    
    return mayor*100 + menor 

continuar = True
n_ordenadas=0
n_desordenadas=0
while continuar:
    entrada = input("Numero: ")
    if entrada == 'FIN':
        continuar = False 
    else:
        numero = str(entrada)
        password = crear_password(numero)
        if ordenado(password):
            n_ordenadas += 1
        else:
            n_desordenadas +=1

print('Hay',n_ordenadas+n_desordenadas,'passwords')
print(n_ordenadas,'ordenadas')
print(n_desordenadas,'no ordenadas')


#Pregunta 1.1
ingresos = 'Juan Gallardo,2020-04-01,08:30;Ana Carmona,2020-04-01,08:35;Juan Gallardo,2020-04-01,10:15;'
ingresos2= 'Perico de los Palotes,2020-05-10,08:30;Ada Lovelace,2020-05-11,11:30;Pythonio Algoritmio,2020-05-11,08:35;Alan Turing,2020-05-10,09:30;Covidio Pandemio,2020-05-08,10:15;Ada Lovelace,2020-05-12,08:30;Guido van Rossum,2020-05-10,15:30;Leonhard Euler,2020-05-10,08:45;Ada Lovelace,2020-05-11,15:30;Pythonio Algoritmio,2020-05-02,17:35;Guido van Rossum,2020-05-11,20:30;'

nombre_sol = input('Ingrese nombre: ')
fecha_sol  = input('Ingrese fecha: ')

j = 0 # posicion donde comienza el registro
k = 0 # posicion de la primera coma
i = 0 # iterador del string
nombre=''
fecha=''
hora =''
horas_ingreso = ''
primera_coma = True # indica si estamos leyendo la 1ra ,
while i < len(ingresos):
    caracter = ingresos[i]
    if caracter == ',' and primera_coma:
        k = i
        nombre = ingresos[j:k]
        fecha =ingresos[k+1:k+1+10]
        hora = ingresos[k+12:k+12+5]
        primera_coma = False
        # Ya se saben los datos se verifica lo solicitado
        if nombre==nombre_sol and fecha==fecha_sol:
            horas_ingreso += hora + ' '
    if caracter ==';':
        j = i+1
        primera_coma = True
    
    i+=1
if horas_ingreso =='':
    horas_ingreso = 'Sin ingresos'
print('Ingresos de',nombre_sol,'en',fecha_sol+':',horas_ingreso)    

#Pregunta 1.2

ingresos = 'Juan Gallardo,2020-04-01,08:30;Ana Carmona,2020-04-01,08:35;Juan Gallardo,2020-04-01,10:15;'
ingresos2= 'Perico de los Palotes,2020-05-10,08:30;Ada Lovelace,2020-05-11,11:30;Pythonio Algoritmio,2020-05-11,08:35;Alan Turing,2020-05-10,09:30;Covidio Pandemio,2020-05-08,10:15;Ada Lovelace,2020-05-12,08:30;Guido van Rossum,2020-05-10,15:30;Leonhard Euler,2020-05-10,08:45;Ada Lovelace,2020-05-11,15:30;Pythonio Algoritmio,2020-05-02,17:35;Guido van Rossum,2020-05-11,20:30;'

fecha_sol  = input('Ingrese fecha: ')

j = 0 # posicion donde comienza el registro
k = 0 # posicion de la primera coma

i = 0 # iterador del string
nombre=''
fecha=''
hora =''
nombres_ingresos = ''
primera_coma = True # indica si estamos leyendo la 1ra ,
while i < len(ingresos):
    caracter = ingresos[i]
    if caracter == ',' and primera_coma:
        k = i
        nombre = ingresos[j:k]
        fecha =ingresos[k+1:k+1+10]
        primera_coma = False
        if nombre not in nombres_ingresos and fecha==fecha_sol:
            nombres_ingresos += nombre+';'
    if caracter ==';':
        j = i+1
        primera_coma = True
    
    i+=1
if nombres_ingresos == '':
    print('No hay ingresos')
else:
    print('Personas que ingresaron:')
    print(nombres_ingresos)




