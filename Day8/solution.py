file = open("inputD8.txt", "r")
lines=file.readlines()

lineas2= [linea.strip().split(',') for linea in lines]
digit_list_list = []
for number_str in lineas2:
    digit_list = list(map(int, number_str[0]))
    digit_list_list.append(digit_list)
transposed_matrix = list(map(list, zip(*digit_list_list)))
# print(transposed_matrix)

arbolesVisibles=0
edge=0
for i,line in enumerate(lines):
    line=line.strip()
    edge+=2
    # print(line)
    if i!=0 and i!=len(lines)-1:
        # print(line.strip())
        #vemos árboles en fila
        for idx, itemFila in enumerate(line):
            # print("estamos en indice, item:", idx, itemFila)
            if idx!=0 and idx!=len(line)-1:
                str_izq=list(line[:idx])
                int_izq = list(map(int, str_izq))
                str_drch=list(line[idx+1:])
                int_drch = list(map(int, str_drch))
                if int(itemFila) > max(int_izq) or int(itemFila) > max(int_drch) :
                    arbolesVisibles +=1
                    # print("suma+1 en fila")
                else:
                    # Comprobamos columna
                    if int(itemFila) > max(transposed_matrix[idx][:i]) or int(itemFila) > max(transposed_matrix[idx][i+1:]):
                        arbolesVisibles +=1
                        # print("contamos en columna")
            # else:
            #     print("no contamos")
                
    else:
        edge+=len(lines)-2
        # print("sumamos edge", edge )
print(arbolesVisibles + edge)


            
