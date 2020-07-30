# -*- coding: utf-8 -*-


pierwsze = []
liczba = 2
while liczba != 2000000:
    lista_pom = []
    flaga = True
    for i in range(2,int(liczba**(0.5))+1):
        if liczba%i != 0:
            continue
        else:
            flaga = False
            break
    if flaga:
        pierwsze.append(liczba)
    liczba += 1
        
print(sum(pierwsze))