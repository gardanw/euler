# -*- coding: utf-8 -*-
import numpy as np

def l_pierwsza(liczba):
    flaga = 0
    for i in range(2,int(np.sqrt(liczba))):
        if liczba%i == 0:
            flaga += 1
    return flaga

def dzielniki(liczba, pierwsze):
#    if l_pierwsza(liczba) == 0:
        
    pom = int(liczba/2)
    for i in range(int(liczba/2), liczba):
        if pom in pierwsze:
            break
        else:
            pom += 1
    p = pierwsze[pierwsze.index(pom)::-1]
    for i in p:
        if liczba%i == 0:
            dziel = i
            return dziel
    return 1
j = 1
lista = [2]
for i in range(2, 101):
    dziel = dzielniki(i, lista)
#    print(i, dziel, np.sqrt(i))
    if dziel != 1 and dziel < np.sqrt(i):
        print(i, np.sqrt(i), dziel)
        j += 1
    elif dziel == 1:
        lista.append(i)
        if len(lista)%5000 == 0:
            print(j, i)
print(j, lista)