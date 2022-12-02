
file=open('inputD2.txt','r')
lines=file.readlines()

# dic={"A":1, "B":2, "C":3, "X":1, "Y":2, "Z":3} #piedra/papel/tijera. XC, YA, ZB

#RETO 1:
nuevaData=[]
puntuacion =[]
for data in lines:
    nuevaData.append(data.replace("A","1").replace("B","2").replace("C","3").replace("X","1").replace("Y","2").replace("Z","3"))

print(nuevaData)
for data in nuevaData:
    if ((data[2]=="1" and data[0]=="3") or (data[2]=="2" and data[0]=="1") or (data[2]=="3" and data[0]=="2")):
        puntuacion.append(6 + int(data[2]))
    elif int(data[0]) == int(data[2]):
        puntuacion.append(3 + int(data[2]))
    else:
        puntuacion.append(int(data[2]))
# print(puntuacion, "res")
print(sum(puntuacion), "Part1")

#RETO 2:
# X(1) means you need to lose, Y(2) means you need to end the round in a draw, and Z(3) means you need to win

resultado=0
for data in nuevaData:
    if(data[2]=='2'):
        resultado+= int(data[0]) +3
    elif(data[2]=='1'):
        if data[0]=='1':
            resultado+=3
        elif data[0]=='2':
            resultado+=1
        else:
            resultado+=2
    else:
        if data[0]=='1':
            resultado+=2+6
        elif data[0]=='2':
            resultado+=3+6
        else:
            resultado+=1+6

print(resultado, "Part2")
