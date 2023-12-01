file=open("inputD5.txt","r")
lines=file.readlines()

stacks = []
for i in range(len(lines[0])):
    # Inicializa un array vacío y lo agrega a la lista de arrays
    stacks.append([])

#armamos arrays con la situación de las pilas inicialmente
for line in lines[:8]:
    line2 = line.replace("["," ").replace("]"," ")
    for idx,char in enumerate(line2):
        if char!=' ' and char!='\n':
            stacks[idx].append(char)
#Eliminamos arrays vacíos
stacks = list(filter(bool, stacks))
# print(stacks)

#Extraemos los números de las órdenes:
movimientos=[]
for line in lines[10:]:
    # frase = "move 15 from 3 to 9"
    numeros = line.split()
    resultado = []
    for numero in numeros:
        if numero.isdigit():
            resultado.append(int(numero))
    movimientos.append(resultado)
# print(movimientos)

# movimiento[0] es la cantidad de elementos a mover
# movimiento[1] es la pila de origen
# movimiento[2] es la pila de destino

movimientosEXAMPLE=[[3, 8, 1],[11,1,8]]
for movimiento in movimientos:
        # print(stacks[movimiento[2]-1], stacks[movimiento[1]-1], "PRINT1")
        for index in range(movimiento[0],0,-1):
            stacks[movimiento[2]-1].insert(0,stacks[movimiento[1]-1][index-1])
        del stacks[movimiento[1]-1][0:movimiento[0]]
        # print(stacks[movimiento[2]-1], stacks[movimiento[1]-1], "PRINT1 DESP")
print(stacks)

#Solución parte1 = VGBBJCRMN
solucion=''
for item in stacks:
    solucion+=item[0]
print(solucion)
