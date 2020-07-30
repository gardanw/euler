# -*- coding: utf-8 -*-
def odczytywanie_z_pliku(plik):
    z_pliku = open(plik)
    lista_slow = []
    for linia in z_pliku:
        pomocnicza = []
        for i in range(len(linia)):
            if linia[i] != '"' and linia[i] != ',':
                pomocnicza.append(linia[i])
            elif linia[i] == ',':
                lista_slow.append(''.join(pomocnicza))
                pomocnicza = []
    lista_slow.append(''.join(pomocnicza))
    return lista_slow

alfabet = {}
for i in range(26):
    alfabet[chr(65+i)] = i + 1

slowa = odczytywanie_z_pliku('p022_names.txt')
#slowa.append('ALONSO')

slowa.sort()
#print(slowa)
print(slowa.index("ALONSO")+1)
print(alfabet)
for i in range(len(slowa)):
    sum_pom = 0
    for j in range(len(slowa[i])):
        sum_pom += alfabet[slowa[i][j]]
#    print(sum_pom, slowa[i], i)
    slowa[i] = sum_pom*(i+1)
print(sum(slowa))
#print(slowa)