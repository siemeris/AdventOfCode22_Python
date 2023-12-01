file=open('inputD6.txt','r')
data=file.read()
print(data)

#PART1
for idx,char in enumerate(data):
    if idx==len(data)-4:
        print("lista fin", idx)
        break
    # elif char!=data[idx+1] and char!=data[idx+2] and char!=data[idx+3]:
    elif len(set([char, data[idx+1], data[idx+2],data[idx+3]]))==4:
        print(idx+4, char, data[idx+1], data[idx+2],data[idx+3])
        break
#Solución parte1 = 1794


#PARTE2, para 14 caracteres y mejorando la solución anterior:
def find_start_of_packet_marker(s):
  # Recorremos la cadena de caracteres en bloques de cuatro caracteres
  for i in range(0, len(s) - 13):
    # Verificamos si los cuatro caracteres son todos diferentes
    if len(set(s[i:i+14])) == 14:
      # Si lo son, devolvemos el número de caracteres procesados hasta ese punto
      return i+14
  # Si no encontramos una combinación de cuatro caracteres que cumplan con el criterio,
  # devolvemos 0
  return 0
print(find_start_of_packet_marker(data)) # 

