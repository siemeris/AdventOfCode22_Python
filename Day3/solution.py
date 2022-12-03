file = open('inputD3.txt','r')
lines = file.readlines()

#PART1
def pesoLetra(letra):
    minus = list(map(chr, range(97, 123)))
    mayus = list(map(chr, range(65, 91)))
    alfabeto = minus + mayus
    peso = alfabeto.index(letra)
    return peso+1

pesoTotal=0
for line in lines:
    m=len(line)//2
    letraEncontrada=''
    for letraEn1 in line[0:m]:
        for letraEn2 in line[m:]:
            if letraEn1==letraEn2 and letraEn1!=letraEncontrada:
                letraEncontrada=letraEn1
                pesoTotal+= pesoLetra(letraEn1)
print(pesoTotal)
#Resultado PARTE1 = 8053

#PART2
pesoTotalParte2=0
for idx, line in enumerate(lines):
    letras=''
    letraEncontradaParte2=''
    if idx==0 or idx%3==0:
        # print(lines[idx],lines[idx+1],lines[idx+2])
        for letra1 in lines[idx]:
            for letra2 in lines[idx+1]:
                if letra1==letra2 and letra1 !='\n':
                    letras+=letra1
            for letra3 in lines[idx+2]:
                if letras.find(letra3)!=-1 and letra3!=letraEncontradaParte2:
                    letraEncontradaParte2=letra3
                    pesoTotalParte2+=pesoLetra(letraEncontradaParte2)
                    # print(letraEncontradaParte2, "ENCONTRADA")
print(pesoTotalParte2)
#Resultado PARTE2 = 2425



