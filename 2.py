# -*- coding: utf-8 -*-

lista = [1,2]

old1 = 1
old2 = 2
new = old1 + old2


while new < 4000000:
    if new%2 == 0:
        lista.append(new)
    old1 = old2
    old2 = new
    new = old1 + old2
    
print(lista, new, old1, old2, sum(lista)-1)