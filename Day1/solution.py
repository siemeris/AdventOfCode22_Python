file = open('input.txt', 'r')
lines = file.readlines()

# PARTE 1
suma=0
renos=[]

for item in lines:
    if item == '\n':
        renos.append(suma)
        suma=0
    else:
        suma+=int(item)

print(max(renos))

# PARTE 2
renos_ordenados = sorted(renos, reverse=True)
print(renos_ordenados)

sumaTop3=0
for i in range(3):
    sumaTop3+=renos_ordenados[i]
print(sumaTop3)
    
