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
contadorIzq=0
contadorDrch=0
contadorUp=0
contadorBot=0
puntuacion=0
for i,line in enumerate(lines):
    line=line.strip()
    edge+=2
    if i!=0 and i!=len(lines)-1:
        for idx, itemFila in enumerate(line):
            print("estamos en indice, item:", idx, itemFila)
            if idx!=0 and idx!=len(line)-1:
                int_izq = list(map(int, list(line[:idx])))
                int_izq.reverse()
                int_drch = list(map(int, list(line[idx+1:])))
                int_up = transposed_matrix[idx][:i]
                int_up.reverse()
                int_bot = transposed_matrix[idx][i+1:]
                contadorDrch=0
                contadorIzq=0
                contadorUp=0
                contadorBot=0
                print(int_up)
                print(int_bot)
                for item in int_izq:
                    print(contadorIzq, item, int_izq, "izq inicio")
                    if item<int(itemFila):
                        contadorIzq+=1
                    elif item == int(itemFila) or item > int(itemFila):
                        contadorIzq+=1
                        break
                    else:
                        break
                print(contadorIzq, "izq")
                for item in int_drch:
                    print(contadorDrch, item, int_drch, "drch inicio")
                    if item<int(itemFila):
                        contadorDrch+=1
                        print(contadorDrch)
                    elif item == int(itemFila) or item > int(itemFila):
                        contadorDrch+=1
                        break

                print(contadorDrch, "drch")
                
                for item in int_up:
                    if item<int(itemFila):
                        contadorUp+=1
                    elif item == int(itemFila) or item > int(itemFila):
                        contadorUp+=1
                        break
                    else:
                        break
                print(contadorUp, "up")

                for item in int_bot:
                    if item<int(itemFila):
                        contadorBot+=1
                    elif item == int(itemFila) or item > int(itemFila):
                        contadorBot+=1
                        break
                    else:
                        break
                print(contadorBot, "bot")


                print(contadorDrch*contadorIzq*contadorBot*contadorUp, "puntuación")
                if puntuacion<contadorDrch*contadorIzq*contadorBot*contadorUp:
                    puntuacion=contadorDrch*contadorIzq*contadorBot*contadorUp
                
print(puntuacion, "resultado")
# 172224
                

