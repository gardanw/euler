# -*- coding: utf-8 -*-


pierwsze = []
liczba = 2
while len(pierwsze) != 10001:
    lista_pom = []
    for i in range(1,int(liczba**(0.5))+1):
        if liczba%i == 0:
            lista_pom.append(i)
    if len(lista_pom) == 1:
        pierwsze.append(liczba)
    liczba += 1
        
print(len(pierwsze), pierwsze[-1])