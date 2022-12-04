file=open("inputD4.txt", "r")
lineas = file.readlines()

# PARTE 1
lineas2= [linea.replace('-',',').split(',') for linea in lineas]
arrEnteros = list(map(lambda x : [int(item) for item in x], lineas2))

contador=0
contadorParte2=0
for item in arrEnteros:
    lista1=list(range(item[0],item[1]+1))
    lista2=list(range(item[2],item[3]+1))
    print(lista1, lista2)
    if all(item in lista1 for item in lista2) or all(item in lista2 for item in lista1):
        contador+=1
    if any(item in lista1 for item in lista2) or any(item in lista2 for item in lista1):
        contadorParte2+=1
print(contador) 
print(contadorParte2)
#Solución PARTE 1 = 602
#Solución PARTE 2 = 891




