# -*- coding: utf-8 -*-
lista = [2]
while len(lista) != 20:
    x = sum(lista)
    y = lista[-1]*2
    print(x,y, (x+y))
    lista.append((x+y))
print(len(lista),lista[-1])

z = 1
for i in range(20):
    z *= (40 - i)
print(z)