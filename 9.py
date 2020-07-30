# -*- coding: utf-8 -*-


n = 1
m = 2
flaga = True
lista = []
while flaga:
    for i in range(500):
        for j in range(500): 
            for c in range(500):
                if i + j + c == 1000 and i**2 + j**2 == c**2:
                    lista.append((i,j,c))
                    break
    break
    
print(lista)