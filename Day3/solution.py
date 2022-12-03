file = open('inputD3.txt','r')
lines = file.readlines()

#PART1
def pesoLetra(letra):
    minus = list(map(chr, range(97, 123)))
    mayus = list(map(chr, range(65, 91)))
    alfabeto = minus + mayus
    peso = alfabeto.index(letra)
    print(peso, "peso")
    return peso+1

pesoTotal=0
for line in lines:
    m=len(line)//2
    letraEncontrada=''
    for letraEn1 in line[0:m]:
        for letraEn2 in line[m:]:
            if letraEn1==letraEn2 and letraEn1!=letraEncontrada:
                print(letraEn1, letraEncontrada, "hola?")
                letraEncontrada=letraEn1
                pesoTotal+= pesoLetra(letraEn1)
print(pesoTotal)

#PART2